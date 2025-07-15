from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from settings.models import WordsSettings


# When registering the user, creates the default by default
# In the user settings
@receiver(post_save, sender=User)
def create_default_words_settings(sender, instance, created, **kwargs):
    if created:
        WordsSettings.objects.get_or_create(
            user=instance,
            defaults={
                "number_words": 20,
                "number_repetitions": 2,
                "translation_list": True,
            },
        )
