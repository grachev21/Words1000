from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class WordsSettings(models.Model):
    TRANSLATION_CHOICES = [
        (True, "Показывать перевод в списке слов"),
        (False, "Спрятать перевод в списке слов"),
    ]
    NUMBER_REPETITIONS_CHOICES = [
        ("1", "Слабо 3 раза"),
        ("2", "Нормально 5 раз"),
        ("3", "Хорошо 6 раз"),
        ("4", "Отлично 8 раз"),
        ("5", "Максимальный результат 10 раз"),
    ]
    number_words = models.IntegerField(
        default=20,
        validators=[MaxValueValidator(100), MinValueValidator(5)],
        verbose_name="Количество слов за день",
    )

    number_repetitions = models.CharField(
        max_length=1,
        choices=NUMBER_REPETITIONS_CHOICES,
        default=3,
        verbose_name="Как хорошо вы хотите запомнить слово",
    )
    translation_list = models.BooleanField(
        choices=TRANSLATION_CHOICES,
        default=True,
        verbose_name="Спрятать/Показать перевод в списке слов",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
