from users.models import WordsUser
from settings.models import WordsSettings
from core.models import WordsCard
import random


class SettingsMixin:

    @staticmethod
    def delite_list_words(form, user):
        """Deleys all records in 'WordsUser'
        Args:
            form (object): Data from the form.
            user (object): User.
        """
        # Checking the form
        if form.cleaned_data["status"] and form.cleaned_data["yes"] == "yes":
            # We get the number of words from the user settings WordsSettings
            (
                WordsSettings.objects.filter(user=user)
                .last()
                .number_words
            )
            # We delete all user words
            WordsUser.objects.filter(user=user).delete()

    @staticmethod
    def get_random_list(user):
        """
        Creates a random list with words.
        Args:
            user (object): User.
        """
        random_elements = random.sample(
            list(WordsCard.objects.all()), 1000
        )
        for element in random_elements:
            print("random elements", element)
            WordsUser.objects.create(
                user=user, core_words=element
            )

    @staticmethod
    def installation_status(user):
        """
        Sets the status of all words by default in WordsUser.
        """
        # Number all the statuses of words
        for status_zero in WordsUser.objects.filter(user=user):
            status_zero.status = "1"
            status_zero.save()

        # Number of words per day
        limiter = WordsSettings.objects.filter(user=user).latest("id").number_words
        # We set the status only to the number of words indicated in number_words
        for status_change in WordsUser.objects.filter(user=user, status="1")[:int(limiter)]:
            print("install status...")
            # Set the status - study
            status_change.status = "2"
            status_change.save()
