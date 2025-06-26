from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from core.models import WordsCard
from django.utils import timezone


class WordsSettings(models.Model):
    number_words = models.IntegerField(
        default=20,
        validators=[MaxValueValidator(100), MinValueValidator(5)],
        verbose_name="Количество слов за день",
    )
    number_repetitions = models.IntegerField(verbose_name="Количество повторов")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Количество слов за день"
        verbose_name_plural = "Количество за день"


class WordsUser(models.Model):
    date = models.DateTimeField(default=timezone.now)
    number_repetitions = models.IntegerField(
        default=3, verbose_name="Количество повторов"
    )
    status = models.BooleanField(default=False, verbose_name="Запомнил")
    show = models.BooleanField(default=True, verbose_name="Показать")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    core_words = models.ForeignKey(WordsCard, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Накопитель слов"
        verbose_name_plural = "Накопитель слов"
