from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import WordsCard
from users.models import WordsUser
from settings.models import WordsSettings
import random
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_save, sender=WordsUser)
def words_user_save(sender, instance, created, **kwargs):
    """
    Обрабатывает сохранение WordsUser

    """

    # Если истина то это при создании, если ложь то это при обновлении

    # Получаем настройки для конкретного пользователя
    user_settings = WordsSettings.objects.get(user=instance.user)
    if created:
        pass

    else:
        try:

            if instance.number_repetitions >= user_settings.number_repetitions:
                print(
                    f"Слово {instance.core_words} достигло нужного количества повторений"
                )
                # Можно изменить статус слова на "изучено"
                instance.status = (
                    "2"  # Предполагая, что '2' - статус изученного
                )
                instance.save()
        except WordsSettings.DoesNotExist:
            print(f"Для пользователя {instance.user} не найдены настройки")
