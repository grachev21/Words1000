from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Word_status(models.Model):
    '''Статус слов'''
    status = models.CharField(max_length=100, blank=True,
                              verbose_name='Статус слова')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус слова'
        verbose_name_plural = 'Статус слов'


class WordsCard(models.Model):
    '''Главная база 1000 слов'''
    word_en = models.CharField(blank=True, max_length=100,
                               verbose_name='На аглийском')
    transcription = models.CharField(blank=True, max_length=100,
                                     verbose_name='Транскрипция')
    word_ru = models.CharField(blank=True, max_length=100,
                               verbose_name='На русском')
    phrases_en = models.TextField(blank=True,
                                  verbose_name='Фразы на английском')
    phrases_ru = models.TextField(blank=True,
                                  verbose_name='Фразы на русском')

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return self.word_en


class IntroductionWords(models.Model):
    '''База слов для ознокомления'''
    word_en = models.CharField(max_length=100, verbose_name='На английском')
    transcription = models.CharField(max_length=100,
                                     verbose_name='Транскрипция')
    word_ru = models.CharField(max_length=100, verbose_name='На русском')

    class Meta:
        verbose_name = 'Слова для ознакомления'
        verbose_name_plural = 'Слова для ознакомления'


class Word_Accumulator(models.Model):
    '''Общий накопитель слов'''
    word = models.CharField(max_length=100, verbose_name='Слово')
    word_status = models.ForeignKey(Word_status,
                                    on_delete=models.PROTECT,
                                    blank=True,
                                    verbose_name='Статус слова')

    class Meta:
        verbose_name = 'Накопитель слов'
        verbose_name_plural = 'Накопитель слов'


class SettingsWordNumber(models.Model):
    '''Количество слов за день'''
    number_words = models.IntegerField(default=20,
                                       validators=[MaxValueValidator(100),
                                                   MinValueValidator(5)],
                                       verbose_name='Количество слов за день')

    class Meta:
        verbose_name = 'Количество слов за день'
        verbose_name_plural = 'Количество за день'


class WordsToRepead(models.Model):
    '''Слова для повторения'''
    word = models.CharField(max_length=100, verbose_name='Слово')

    class Meta:
        verbose_name = 'Слово для повторения'
        verbose_name_plural = 'Слова для повторения'


class WordReadingPractice(models.Model):
    '''База слов для чтения'''
    word = models.CharField(max_length=100, verbose_name='Слово')

    class Meta:
        verbose_name = 'Слово для чтения'
        verbose_name = 'Слова для чтения'
