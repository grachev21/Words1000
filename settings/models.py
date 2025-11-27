from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class WordsSettings(models.Model):
    """
    Keeps user settings
    """

    TRANSLATION_CHOICES = [
        (True, "Показывать перевод в списке слов"),
        (False, "Спрятать перевод в списке слов"),
    ]
    NUMBER_REPETITIONS_CHOICES = [
        ("1", "Слабый уровень:  3 повторения"),
        ("2", "Нормально уровень: 5 повторений"),
        ("3", "Хорошо уровень: 6 повторений"),
        ("4", "Отлично: 8 повторений"),
        ("5", "Максимальный результат: 10 повторений"),
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
    number_write = models.IntegerField(default=5)
    max_number_read = models.IntegerField(default=10, validators=[MaxValueValidator(30)])
    translation_list = models.BooleanField(
        choices=TRANSLATION_CHOICES,
        default=True,
        verbose_name="Спрятать/Показать перевод в списке слов",
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
