from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in 
from django.dispatch import receiver
from core.models import WordsCard
from users.models import WordsUser
import random
from django.contrib.auth import get_user_model
import logging

# We get a model of the user DJango
User = get_user_model()

# Logger Setting for this module
logger = logging.getLogger(__name__)

def create_initial_words_for_user(user, words_count=1000):
    """
    Creates an initial set of words for the user.

    Args:
    user: an object of a user for which words are created
    Words_count: The maximum number of words for creation (default 1000)
    """
    all_words = WordsCard.objects.all()
    if all_words.exists():
        # We determine the number of words for sample (no more than the total number of words)
        sample_size = min(words_count, all_words.count())
        random_words = random.sample(list(all_words), sample_size)
        
        # Mass creation of user-word ties for performance
        WordsUser.objects.bulk_create([
            WordsUser(user=user, core_words=word)
            for word in random_words
        ])

@receiver(post_save, sender=User)
def handle_user_creation(sender, instance, created, **kwargs):
    """
    Post_save signal processor for user model.
    Creates an initial set of words when creating a new user.
    """
    if created:
        logger.info(f"Creating initial words for new user: {instance.username}")
        create_initial_words_for_user(instance)


# If suddenly at the time the base is empty
@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    """
    User entry signal processor.
    Checks and creates an initial set of words if the user does not have them.
    Passes super -users.
    """
    if not user.is_superuser:
        if not WordsUser.objects.filter(user=user).exists():
            logger.info(f"No words found for user {user.username}, creating initial set")
            create_initial_words_for_user(user)
