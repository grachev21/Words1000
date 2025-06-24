from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


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


class IntroductionWords(models.Model):
    word_en = models.CharField(max_length=100, verbose_name="На английском")
    transcription = models.CharField(max_length=100, verbose_name="Транскрипция")
    word_ru = models.CharField(max_length=100, verbose_name="На русском")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Слова для ознакомления"
        verbose_name_plural = "Слова для ознакомления"


class Word_Accumulator(models.Model):
    word_en = models.CharField(max_length=100, verbose_name="Слово на английском")
    word_ru = models.CharField(max_length=100, verbose_name="Слово на русском")
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Накопитель слов"
        verbose_name_plural = "Накопитель слов"


class SettingsWordNumber(models.Model):
    number_words = models.IntegerField(
        default=20,
        validators=[MaxValueValidator(100), MinValueValidator(5)],
        verbose_name="Количество слов за день",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Количество слов за день"
        verbose_name_plural = "Количество за день"


class RepeatNumber(models.Model):
    number = models.CharField(max_length=100, verbose_name="Номер повтора")

    class Meta:
        verbose_name = "Номер повтора"
        verbose_name_plural = "Номера повтора"

    def __str__(self):
        return self.number


class WordsToRepeat(models.Model):
    word = models.CharField(max_length=100, verbose_name="Слово")
    repeat_number = models.ForeignKey(RepeatNumber, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Слово для повторения"
        verbose_name_plural = "Слова для повторения"


class WordsConfigJson(models.Model):
    WORD_DATA = models.JSONField(null=True)
    WORD_USER = models.JSONField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Config"
        verbose_name = "Configs"
