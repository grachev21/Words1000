from users.models import WordsUser
from core.models import WordsCard
from settings.models import WordsSettings

import random


class GameInitMixin:
    """Mixin for initializing game data with words and phrases."""

    @staticmethod
    def get_random_user_word(user):
        """Returns one correct word from the studied words model/WordsUser"""
        learned_words = WordsUser.objects.filter(user=user, status="2")
        return random.choice(learned_words) if learned_words else None

    @staticmethod
    def get_random_words(exclude_word_id):
        """Get random words excluding the specified one model/WordsCard"""
        available_words = WordsCard.objects.exclude(id=exclude_word_id)
        return random.sample(
            list(available_words), min(3, len(available_words))
        )

    @staticmethod
    def mixer_words(list_words, word):

        # We form a mixed list with words for tests
        for_random = [(f"false_{word}", word) for word in list_words] + \
            [("true", WordsCard.objects.get(id=word.core_words.id))]

        for_result = random.sample(for_random, len(for_random))

        return {
            f"option_{item[0]}": {
                "id": item[1].id,
                "en": item[1].word_en,
                "ru": item[1].word_ru,
                "transcription": item[1].transcription,
                "phrase": [
                    n for n in zip(item[1].phrases_en, item[1].phrases_ru)
                ],
            }
            for item in for_result
        }

    def init_data(self, user, context):
        """Initialize game data and update context"""
        if not user or not context:
            return context

        word_user = self.get_random_user_word(user)
        three_random_words = self.get_random_words(word_user.core_words.id)

        mixer_words = self.mixer_words(
            list_words=three_random_words, word=word_user
        )

        if not word_user:
            return context

        # Prepare context data
        context.update({
            "mixer_words": mixer_words,
            "number_repetitions": WordsSettings.objects.filter(user=user).first().number_repetitions,
            "words_user": WordsUser.objects.filter(user=user),

        })

        return context
