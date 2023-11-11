from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User 
from django.utils import timezone


class WordsCard(models.Model):
    '''
    Основная модель в которой хранится вся база знаний.
    '''
    word_en = models.JSONField(blank=True, verbose_name='Английский')
    word_ru = models.JSONField(blank=True, verbose_name='Русский')
    transcription = models.JSONField(blank=True, verbose_name='Транскрипция')
    phrases_en = models.JSONField(blank=True, verbose_name='Фразы-Английский')
    phrases_ru = models.JSONField(blank=True, verbose_name='Фразы-Русский')

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return self.word_en

class IntroductionWords(models.Model):
    '''
    Связь с классоь User один с одним.
    Связь с моделью UserWords.

    В эту модель добавляются слова для ознакомления перед тестом.
    '''
    word_en = models.CharField(max_length=100, verbose_name='На английском')
    transcription = models.CharField(max_length=100, verbose_name='Транскрипция')
    word_ru = models.CharField(max_length=100, verbose_name='На русском')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Слова для ознакомления'
        verbose_name_plural = 'Слова для ознакомления'


class Word_Accumulator(models.Model):
    '''
    Связь с моделью UserWords.

    В этой модели, накапливаются угаданные слова пользователя
    для дальнейшего повторения и отображения статуса.
    attr - word_en, word_ru, users.
    '''
    word_en = models.CharField(max_length=100, verbose_name='Слово на английском')
    word_ru = models.CharField(max_length=100, verbose_name='Слово на русском')
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Накопитель слов'
        verbose_name_plural = 'Накопитель слов'


class SettingsWordNumber(models.Model):
    '''
    Связь с классом User один с одним.
    В эту модель, через настройки записывается количество слов, которые пользователь должен изучить за один день.
     Связь с моделью UserWords.

    В эту модель, через настройки записывается количество слов, которые
    пользователь должен изучить за один день.
    attr - number_words, users
    '''
    number_words = models.IntegerField(default=20, validators=[MaxValueValidator(100), MinValueValidator(5)], verbose_name='Количество слов за день')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Количество слов за день'
        verbose_name_plural = 'Количество за день'


class RepeatNumber(models.Model):
    '''
    Эта модель расширяет класс модели WordsToRepeat
    '''
    number = models.CharField(max_length=100, verbose_name='Номер повтора')

    class Meta:
        verbose_name = 'Номер повтора'
        verbose_name_plural = 'Номера повтора'

    def __str__(self):
        return self.number


class WordsToRepeat(models.Model):
    '''
    Связь с моделью UserWords.

    В эту модель, добавляется то количество слов которое user установил в настройках.
    У каждого слова есть свой статус - zero, one, two, tree. При достижении
    последнего слово удаляется из поля.
    '''
    word = models.CharField(max_length=100, verbose_name='Слово')
    repeat_number = models.ForeignKey(RepeatNumber, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Слово для повторения'
        verbose_name_plural = 'Слова для повторения'


class WordsConfigJson(models.Model):
    '''
    Связь с моделью UserWords.

    Эта модель получает, вариант слова от пользователя и сохраняет его в
    поле WORD_USER.

    WORD_DATA, это набор данных в реальном времени полученных из модуля
    play_on_words - в него входят:
    1. правильный вариант слова;
    2. три не правильных варианта слова;
    3. рандомный список из всех слов
    '''
    WORD_DATA = models.JSONField(null=True)
    WORD_USER = models.JSONField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Config'
        verbose_name = 'Configs'


    # class EmailRegister(AbstractUser):
    #     username = models.CharField(
    #         ("username"),
    #         max_length=150,
    #         help_text=(
    #             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    #         ),
    #         validators=[AbstractUser.username_validator],
    #         error_messages={
    #             "unique": ("A user with that username already exists."),
    #         },
    #         null=True,
    #         blank=True,
    #     )
    #
    #     email = models.EmailField(("email address"), unique=True, )
    #
    #     is_active = models.BooleanField(
    #         ("active"),
    #         default=False,
    #         help_text=(
    #             "Designates whether this user should be treated as active. "
    #             "Unselect this instead of deleting accounts."
    #         ),
    #     )
    #
    #     USERNAME_FIELD = "email"
    #     REQUIRED_FIELDS = []
    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
