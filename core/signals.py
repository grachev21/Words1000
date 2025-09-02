# # Import necessary modules and models
# from django.contrib.auth.signals import user_logged_in  # Signal for user login
# from django.dispatch import (
#     receiver,
# )  # Decorator to connect signals to functions
# from users.models import WordsUser  # User's word model
# from settings.models import WordsSettings  # User settings model
# import random  # For random selection of words
#
#
# @receiver(user_logged_in)  # Decorator to run this function when a user logs in
# def update_user_word_status(sender, request, user, **kwargs):
#     print("signals words app ...")
#     """
#     Updates word status for regular users upon login.
#
#     For non-superusers, selects a random set of words marked with status "1"
#     and updates them to status "2" based on the user's word count setting.
#
#     Args:
#         sender: The model class that sent the signal (User model in this case)
#         request: The current HttpRequest object
#         user: The user instance that just logged in
#         **kwargs: Additional keyword arguments
#     """
#
#     # Skip processing if the user is a superuser/admin
#     if user.is_superuser:
#         return
#
#     # Get all words for the current user with status "1" (active words)
#     active_words = WordsUser.objects.filter(user=user, status="1")
#
#     # If there are no active words, exit the function
#     if not active_words.exists():
#         return
#
#     # Get the latest settings for the current user
#     user_settings = WordsSettings.objects.filter(user=user).last()
#
#     # Select a random sample of words to update:
#     # - Either the number specified in user settings (user_settings.number_words)
#     # - Or all available words if there are fewer than the setting requests
#     words_to_update = random.sample(
#         list(active_words),
#         min(user_settings.number_words, active_words.count()),
#     )
#
#     # Update the selected words' status from "1" to "2"
#     WordsUser.objects.filter(
#         id__in=[word.id for word in words_to_update]
#     ).update(status="2")
#
#
