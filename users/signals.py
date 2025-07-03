from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.models import WordsCard
from users.models import WordsUser
import random
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print("created ...")
        random_elements = random.sample(list(WordsCard.objects.all()), 1000)

        for element in random_elements:

            print("record ...")
            WordsUser.objects.create(user=instance, core_words=element)
