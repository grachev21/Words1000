# users/signals

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


# Special Function for Word incision
def create_initial_words_for_user(user, words_count=1000):
    all_words = WordsCard.objects.all()
    if all_words.exists():
        # We determine the number of words for sample (no more than the total number of words)
        sample_size = min(words_count, all_words.count())
        random_words = random.sample(list(all_words), sample_size)

        # Mass creation of user-word ties for performance
        WordsUser.objects.bulk_create(
            [WordsUser(user=user, core_words=word) for word in random_words]
        )


# Post_save signal processor for user model.
# Creates an initial set of words when creating a new user.
@receiver(post_save, sender=User)
def handle_user_creation(sender, instance, created, **kwargs):
    if created:
        create_initial_words_for_user(instance)


# If suddenly at the time the base is empty
@receiver(user_logged_in)
def handle_user_login(sender, request, user, **kwargs):
    if not user.is_superuser: # If not a super user
        if not WordsUser.objects.filter(user=user).exists(): # If the base is empty  
            create_initial_words_for_user(user)
