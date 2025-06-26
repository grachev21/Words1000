from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class WordsCard(models.Model):
    word_en = models.JSONField(blank=True, verbose_name="Английский")
    word_ru = models.JSONField(blank=True, verbose_name="Русский")
    transcription = models.JSONField(blank=True, verbose_name="Транскрипция")
    phrases_en = models.JSONField(blank=True, verbose_name="Фразы-Английский")
    phrases_ru = models.JSONField(blank=True, verbose_name="Фразы-Русский")

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"

    def __str__(self):
        return self.word_en
