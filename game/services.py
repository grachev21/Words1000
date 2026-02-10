import random

from core.models import WordsCard
from settings.models import WordsSettings
from users.models import WordsUser


class SettingsMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.request = request
            self.user_settings = WordsSettings.objects.filter(user=request.user).latest("id")
            self.get_user_settings()
            return super().dispatch(request, *args, **kwargs)


    def get_user_settings(self):
        settings = self.user_settings
        return {
            "number_words": settings.number_words,
            "number_repetitions": settings.number_repetitions,
            "max_number_read": settings.max_number_read,
            "number_write": settings.number_write,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"user_settings": self.get_user_settings()})
        return context


class GameMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.request = request
            self.user_settings = WordsSettings.objects.filter(user=request.user).first()
            self.words_card = WordsCard.objects.all()
            self.get_random_one_word()
            self.get_three_wrong_words()
        return super().dispatch(request, *args, **kwargs)


    def get_random_one_word(self):
        learned_words = WordsUser.objects.filter(user=self.request.user, status="2")
        self.correct_one_word = random.choice(learned_words) if learned_words else None

    def get_three_wrong_words(self):
        available_words = WordsCard.objects.exclude(
            id=self.correct_one_word.core_words.id
        )
        self.three_wrong_words = random.sample(
            list(available_words), min(3, len(available_words))
        )

    def mixer_words(self):
        for_random = [
            ("true", self.words_card.get(id=self.correct_one_word.core_words.id))
        ]

        # Add incorrect words to it
        for w in self.three_wrong_words:
            for_random.append((f"false", w))

        # Mix all the words
        for_result = random.sample(for_random, len(for_random))

        # List for final result
        result = []
        key = ["a", "s", "d", "f"]
        for index, item in enumerate(for_result):
            result.append(
                {
                    "option": item[0],
                    "id": item[1].id,
                    "en": item[1].word_en,
                    "ru": item[1].word_ru,
                    "transcriptions": item[1].transcription,
                    "key": key[index],
                }
            )

        return result

    def get_phrases(self):
        phrases = []
        en =self.correct_one_word.core_words.phrases_en
        ru =self.correct_one_word.core_words.phrases_ru
        for en_ru in zip(en, ru):
            if len(phrases) != self.user_settings.max_number_read:
                phrases.append(en_ru)
        return phrases


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "correct_word_ru": ", ".join(self.correct_one_word.core_words.word_ru.split(",")[0:3]),
                "correct_word": self.correct_one_word.core_words,
                "phrases": self.get_phrases(),
                "mixer_words": self.mixer_words(),  # Слова
            }
        )
        return context

class ProgressBarGameMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.request = request
        return super().dispatch(request, *args, **kwargs)

    def progress_bar_game(self):
        words_user = WordsUser.objects.filter(user=self.request.user, status=2)
        words_settings = WordsSettings.objects.filter(user=self.request.user).latest("id")
        study = words_user.count()
        studied = words_settings.number_words - study

        return {
            "progress": round(((study - studied) / study) * 100) - 100,
            "remainder": study,
        }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"progress_bar_game": self.progress_bar_game()})
        return context