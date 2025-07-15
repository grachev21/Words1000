# core/models.py
# This file defines the database models for the 'core' app, specifically the
# WordsCard model for storing vocabulary cards.
# Each WordsCard contains English and Russian words, their transcriptions, and example
# phrases in both languages.
from django.db import models


class WordsCard(models.Model):
    # Stores the English word(s) as a JSON object (e.g., list or dict)
    word_en = models.JSONField(blank=True, verbose_name="Английский")
    # Stores the Russian translation(s) as a JSON object
    word_ru = models.JSONField(blank=True, verbose_name="Русский")
    # Stores the transcription(s) of the word(s) as a JSON object
    transcription = models.JSONField(blank=True, verbose_name="Транскрипция")
    # Stores example phrases in English as a JSON object
    phrases_en = models.JSONField(blank=True, verbose_name="Фразы-Английский")
    # Stores example phrases in Russian as a JSON object
    phrases_ru = models.JSONField(blank=True, verbose_name="Фразы-Русский")

    class Meta:
        # Human-readable singular name for the model
        verbose_name = "Слово"
        # Human-readable plural name for the model
        verbose_name_plural = "Слова"

    def __str__(self):
        # String representation of the WordsCard, returns the English word(s)
        return self.word_en
