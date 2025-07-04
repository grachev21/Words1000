from typing import Dict, List, Any
from django.db.models import QuerySet
from settings.models import WordsSettings
from users.models import WordsUser
from core.models import WordsCard
import random


class GameInitMixin:
    """Mixin for initializing game data with words and phrases."""
    
    @staticmethod
    def get_user_words_settings(user) -> WordsSettings:
        """Get words settings for the given user."""
        return WordsSettings.objects.filter(user=user).last()
    
    @staticmethod
    def get_random_user_word(user) -> WordsUser:
        """Get a random word from user's learned words (status=2)."""
        learned_words = WordsUser.objects.filter(user=user, status="2")
        return random.choice(learned_words) if learned_words else None
    
    @staticmethod
    def prepare_phrases(word_user: WordsUser) -> List[Dict[str, str]]:
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
    
    @staticmethod
    def get_random_words(exclude_word_id: int, count: int = 3) -> QuerySet[WordsCard]:
        """Get random words excluding the specified one."""
        available_words = WordsCard.objects.exclude(id=exclude_word_id)
        return random.sample(list(available_words), min(count, len(available_words)))
    
    def init_data(self, user, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Initialize game data and update context.
        
        Args:
            user: Authenticated user
            context: Template context to update
            
        Returns:
            Updated context dictionary
        """
        if not user or not context:
            return context
            
        # Get required data
        words_settings = self.get_user_words_settings(user)
        word_user = self.get_random_user_word(user)
        
        if not word_user:
            return context
            
        # Prepare context data
        context.update({
            "settings": words_settings,
            "three_random_words": self.get_random_words(word_user.core_words.id),
            "correct_word": word_user,
            "phrases": self.prepare_phrases(word_user)
        })
        
        return context