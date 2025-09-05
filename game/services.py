from typing import Dict, List, Any
from django.db.models import QuerySet
from settings.models import WordsSettings
from users.models import WordsUser
from core.models import WordsCard
import random


class GameInitMixin:
    """Mixin for initializing game data with words and phrases."""

    @staticmethod
    def get_user_words_settings(user):
        """Returns the user settings"""
        return WordsSettings.objects.filter(user=user).last()

    @staticmethod
    def get_random_user_word(user):
        """Returns one correct word from the studied words model/WordsUser"""
        learned_words = WordsUser.objects.filter(user=user, status="2")
        return random.choice(learned_words) if learned_words else None


    @staticmethod
    def get_random_words(exclude_word_id):
        """Get random words excluding the specified one model/WordsCard"""
        available_words = WordsCard.objects.exclude(id=exclude_word_id)
        return random.sample(list(available_words), min(3, len(available_words)))
    
    @staticmethod
    def mixer_word(list_words, word):
        result = [(0, l) for l in list_words] + [(1, WordsCard.objects.get(id=word.id))]
        return random.sample(result, len(result))

    @staticmethod
    def prepare_phrases(word_user):
        """Prepare list of phrases with translations."""
        if not word_user or not hasattr(word_user.core_words, 'phrases_en'):
            return []

        return [
            {"en": en_phrase, "ru": ru_phrase}
            for en_phrase, ru_phrase in zip(
                word_user.core_words.phrases_en,
                word_user.core_words.phrases_ru
            )
        ]


    def init_data(self, user, context: Dict[str, Any]) -> Dict[str, Any]:
        """Initialize game data and update context"""
        if not user or not context:
            return context

        # Get required data
        words_settings = self.get_user_words_settings(user)
        word_user = self.get_random_user_word(user)
        three_random_words = self.get_random_words(word_user.core_words.id)
        mixer_word = self.mixer_word(list_words=three_random_words, word=word_user)
        print(mixer_word)
        phrases = self.prepare_phrases(word_user)

        if not word_user:
            return context

        # Prepare context data
        context.update({
            "settings": words_settings,
            "three_random_words": three_random_words,
            "correct_word": word_user,
            "mixer_word": mixer_word,
            "phrases": phrases,

        })

        return context
