from django.db import models


class Word_status(models.Model):
    status = models.TextField(blank=True, verbose_name='Статус слова')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус слова'
        verbose_name_plural = 'Статус слов'

class WordsCard(models.Model):
    word_en = models.CharField(blank=True, max_length=100, verbose_name='На аглийском')
    transcription = models.CharField(blank=True, max_length=100, verbose_name='Транскрипция')
    word_ru = models.CharField(blank=True, max_length=100, verbose_name='На русском')
    phrases_en = models.TextField(blank=True, verbose_name='Фразы на английском')
    phrases_ru = models.TextField(blank=True, verbose_name='Фразы на русском')

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'


    def __str__(self):
        return self.word_en

class Word_Accumulator(models.Model):
    word = models.CharField(max_length=100, verbose_name='Слово')
    number_repetitions = models.TextField(blank=True, verbose_name='Количество повторений')
    word_status = models.ForeignKey(Word_status, on_delete=models.PROTECT, blank=True, verbose_name='Статус слова')

    class Meta:
        verbose_name = 'Накопитель слов'
        verbose_name_plural = 'Накопитель слов'


