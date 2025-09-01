from django.db import models
from django.contrib.auth.models import User
from core.models import WordsCard


class WordsUser(models.Model):
    STATUS_CHOICE = [
        ("1", "Неизвестно"),
        ("2", "Изучаю"),
        ("3", "Повторяю"),
        ("4", "Изучил"),
    ]
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    number_repetitions = models.IntegerField(
        default=0, verbose_name="Количество сделанных повторов"
    )
    status = models.CharField(
        choices=STATUS_CHOICE, max_length=1, default="1", verbose_name="Этап запоминания"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    core_words = models.ForeignKey(WordsCard, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Накопитель слов"
        verbose_name_plural = "Накопитель слов"
