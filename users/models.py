from core.models import WordsCard  # Импорт модели слов из другого приложения
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.conf import (
    settings,
)  # Для динамического указания модели пользователя в ForeignKey


# Кастомный менеджер пользователей — отвечает за создание пользователей и суперпользователей
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Проверяем, что email передан
        if not email:
            raise ValueError("Email обязателен")

        # Нормализуем email (приводим к нижнему регистру и убираем лишние пробелы)
        email = self.normalize_email(email)

        # Создаём объект пользователя с email и дополнительными полями
        user = self.model(email=email, **extra_fields)

        # Устанавливаем пароль (хэшируется)
        user.set_password(password)

        # Сохраняем пользователя в базу
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Устанавливаем необходимые флаги для суперпользователя
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Проверяем, что флаги установлены правильно
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser должен быть staff")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser должен быть superuser")

        # Создаём суперпользователя с указанными параметрами
        return self.create_user(email, password, **extra_fields)


# Кастомная модель пользователя
class User(AbstractBaseUser, PermissionsMixin):
    # Поле email, по которому будет осуществляться вход (уникально)
    email = models.EmailField(unique=True)

    # Имя и фамилия, необязательные для заполнения
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    # Активен ли пользователь (можно блокировать)
    is_active = models.BooleanField(default=False)

    # Является ли пользователь сотрудником (для доступа в админку и т.п.)
    is_staff = models.BooleanField(default=False)

    # Дата регистрации пользователя (автоматически ставится при создании)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Подключаем наш кастомный менеджер для работы с пользователями
    objects = UserManager()

    # Поле, которое будет использоваться для аутентификации (логин по email)
    USERNAME_FIELD = "email"
    # Поля, обязательные для создания пользователя (оставляем пустым, т.к. email — обязательный)
    REQUIRED_FIELDS = []

    def __str__(self):
        # Строковое представление объекта — email пользователя
        return self.email


# Модель, которая хранит информацию о прогрессе пользователя с некоторыми словами
class WordsUser(models.Model):

    # Варианты статуса пользователя по отношению к слову
    class Status(models.IntegerChoices):
        UNKNOWN = 1, "Неизвестно"
        LEARNING = 2, "Изучаю"
        REPETITION = 3, "Повторяю"
        LEARNED = 4, "Изучил"

    # Дата создания записи (автоматически ставится при создании)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Количество сделанных повторов слова пользователем
    number_repetitions = models.IntegerField(
        default=0, verbose_name="Количество сделанных повторов"
    )

    # Статус изучения слова с использованием предопределённых вариантов
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.UNKNOWN,
        verbose_name="Этап запоминания",
    )

    # Связь с пользователем — указываем модель пользователя из настроек, чтобы не жестко привязываться
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Связь со словом из основной модели слов
    core_words = models.ForeignKey(WordsCard, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Накопитель слов"  # Название модели в ед. числе для админки
        verbose_name_plural = (
            "Накопитель слов"  # Название модели во мн. числе для админки
        )
