from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import WordsCard
from users.models import WordsUser
from settings.models import WordsSettings
import random
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    """
    Создает начальный набор слов для нового пользователя
    """
    if created:
        print(f"Создан новый пользователь {instance.username}")
        
        # Более эффективный способ получения случайных слов
        all_words = WordsCard.objects.all()
        if all_words.exists():
            # Берем минимум из 1000 и общего количества слов
            sample_size = min(1000, all_words.count())
            random_words = random.sample(list(all_words), sample_size)
            
            # Массовое создание записей через bulk_create
            WordsUser.objects.bulk_create([
                WordsUser(user=instance, core_words=word)
                for word in random_words
            ])
            print(f"Создано {sample_size} записей WordsUser для пользователя {instance.username}")

@receiver(post_save, sender=WordsUser)
def words_user_save(sender, instance, created, **kwargs):
    """
    Обрабатывает сохранение WordsUser
    """
    if created:
        print(f"Создана новая связь пользователя {instance.user} со словом {instance.core_words}")
    else:
        print(f"Обновлена связь пользователя {instance.user} со словом {instance.core_words}")
        print(f"Текущее количество повторений: {instance.number_repetitions}")
        
        try:
            # Получаем настройки для конкретного пользователя
            user_settings = WordsSettings.objects.get(user=instance.user)
            
            if instance.number_repetitions == user_settings.number_repetitions:
                print(f"Слово {instance.core_words} достигло нужного количества повторений")
                # Можно изменить статус слова на "изучено"
                instance.status = '2'  # Предполагая, что '2' - статус изученного
                instance.save()
        except WordsSettings.DoesNotExist:
            print(f"Для пользователя {instance.user} не найдены настройки")