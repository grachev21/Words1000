from users.models import WordsUser
from core.models import WordsCard
from settings.models import WordsSettings

import random


class GameInitMixin:
    """Mixin for initializing game data with words and phrases."""

    @staticmethod
    def get_random_user_word(user):
        """
        Get all the words from the user database WordsUser and get one
        random word.
        """
        learned_words = WordsUser.objects.filter(user=user, status="2")
        return random.choice(learned_words) if learned_words else None

    @staticmethod
    def get_random_words(exclude_word_id):
        """
        Get random words excluding the specified one model/WordsCard
        """
        available_words = WordsCard.objects.exclude(id=exclude_word_id)
        return random.sample(
            list(available_words), min(3, len(available_words))
        )

    @staticmethod
    def mixer_words(list_words, word):
        """Mixes correct and incorrect words.
        Args:
        list_words : Wrong words
        word : Correct word
        """

        # Create a list with one correct word
        for_random = [("true", WordsCard.objects.get(id=word.core_words.id))]

        # Add incorrect words to it
        for w in list_words:
            for_random.append((f"false", w))

        # Mix all the words
        for_result = random.sample(for_random, len(for_random))

        # List for final result
        result = []
        for item in for_result:

            # Collecting phrases in English and Russian into one card of cards
            # Example ((en, ru), (en, ru)...)
            phrases_list = []
            for en_phrase, ru_phrase in zip(
                item[1].phrases_en, item[1].phrases_ru
            ):
                phrases_list.append((en_phrase, ru_phrase))
            result.append(
                {
                    "option": item[0],
                    "id": item[1].id,
                    "en": item[1].word_en,
                    "ru": item[1].word_ru,
                    "transcriptions": item[1].transcription,
                }
            )

        return result

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
        context.update(
            {
                "correct_word": ", ".join(
                    word_user.core_words.word_ru.split(",")[0:3]
                ),
                "data_for_read": {
                    "correct_word": word_user.core_words,
                    "phrases": [
                        n
                        for n in zip(
                            word_user.core_words.phrases_en,
                            word_user.core_words.phrases_ru,
                        )
                    ],
                },
                "mixer_words": mixer_words,  # Слова
                "number_repetitions": WordsSettings.objects.filter(user=user)
                .first()
                .number_repetitions,
                "words_user": WordsUser.objects.filter(user=user),
            }
        )

        return context
