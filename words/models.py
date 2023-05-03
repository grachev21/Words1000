from django.db import models

class WordsCard(models.Model):
    word_en = models.TextField(blank=True)
    transcription = models.TextField(blank=True)
    word_ru = models.TextField(blank=True)
    phraze_en = models.TextField(blank=True)
    phraze_ru = models.TextField(blank=True)
    number_repetitions = models.TextField(blank=True)

    def __str__(self):
        return self.word_en
