from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from settings.models import WordsSettings
from users.models import WordsUser
from core.services.services_core import create_records_signals 


@receiver(post_save, sender=User)
def user_created(instance, created, **kwargs):
    if created:
        quantity = 20
        WordsSettings.objects.create(
            number_words=quantity,
            number_repetitions="2",
            translation_list=True,
            user=instance,
        )
    
    # create_records_signals(User, quantity)
    # WordsUser.objects.create(
    #             word_en... 
    #             word_ru...     
    #             transcription...
    #             phrases_en...     
    #             phrases_ru... 
    #             )