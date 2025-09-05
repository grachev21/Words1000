from settings.models import WordsSettings
from users.models import WordsUser
from core.models import WordsCard
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model

import logging
import random


# We get a model of the user DJango
User = get_user_model()

# Logger Setting for this module
logger = logging.getLogger(__name__)


# Special Function for Word incision
def create_initial_words_for_user(user, words_count=1000):
    all_words = WordsCard.objects.all()
    if all_words.exists():
        # We determine the number of words for
        # sample (no more than the total number of words)
        sample_size = min(words_count, all_words.count())
        random_words = random.sample(list(all_words), sample_size)

        # Mass creation of user-word ties for performance
        WordsUser.objects.bulk_create(
            [WordsUser(user=user, core_words=word) for word in random_words]
        )

def installation_status(user):
    """
    Sets the status of all words by default in WordsUser.
    """

    # Number of words per day
    lim = int(WordsSettings.objects.filter(user=user).latest("id").number_words)
    # We set the status only to the number of words indicated in number_words
    for status_change in WordsUser.objects.filter(user=user, status="1")[:lim]:
        print("install status...")
        # Set the status - study
        status_change.status = "2"
        status_change.save()


# This signal works when creating
# user, he fills the default settings
@receiver(post_save, sender=User)
def create_default_words_settings(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        print("create settings words for user <<<")
        WordsSettings.objects.get_or_create(
            user=instance,
            defaults={
                "number_words": 20,
                "number_repetitions": 2,
                "translation_list": True,
            },
        )

# Post_save signal processor for user model.
# Creates an initial set of words when creating a new user.
@receiver(post_save, sender=User)
def handle_user_creation(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        create_initial_words_for_user(user=instance)
        installation_status(user=instance)


# # If suddenly at the time the base is empty
# @receiver(user_logged_in)
# def handle_user_login(sender, request, user, **kwargs):
#     if not user.is_superuser:  # If not a super user
#         # If the base is empty
#         if not WordsUser.objects.filter(user=user).exists():
#             create_initial_words_for_user(user)






