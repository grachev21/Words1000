from core.models import WordsCard
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# To dynamically specify the user model in the ForeignKey
from django.conf import settings


# Custom user manager - responsible for creating users and superusers
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Check that the email has been sent
        if not email:
            raise ValueError("Email обязателен")
        # Normalize email (convert to lower case and remove extra spaces)
        email = self.normalize_email(email)
        # Create a user object with email and additional fields
        user = self.model(email=email, **extra_fields)
        # Set the password (hashed)
        user.set_password(password)
        # Save the user to the database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set the necessary flags for the superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        # Check that the flags are set correctly
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser должен быть staff")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser должен быть superuser")
        # Create super useless with parameters
        return self.create_user(email, password, **extra_fields)


# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    # Email field that will be used to log in (unique)
    email = models.EmailField(unique=True)
    # First and last name, optional
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    # Is the user active (can be blocked)
    is_active = models.BooleanField(default=True)
    # Is the user an employee (for access to the admin panel, etc.)
    is_staff = models.BooleanField(default=False)
    # User registration date (automatically set upon creation)
    date_joined = models.DateTimeField(auto_now_add=True)
    # Connect our custom manager to work with users
    objects = UserManager()
    # Field that will be used for authentication (login by email)
    USERNAME_FIELD = "email"
    # Fields required to create a user (leave empty, because email is required)
    REQUIRED_FIELDS = []

    def __str__(self):
        # String representation of the object - user email
        return self.email


# A model that stores information about the user's progress with some words
class WordsUser(models.Model):
    STATUS_CHOICE = [
        ("1", "Неизвестно"),
        ("2", "Изучаю"),
        ("3", "Повторяю"),
        ("4", "Изучил"),
    ]


    # Record creation date (automatically set upon creation)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # Number of repetitions of a word made by the user
    number_repetitions = models.IntegerField(
        default=0, verbose_name="Количество сделанных повторов"
    )

    # Status of word learning using predefined options
    status = models.CharField(
        choices=STATUS_CHOICE, max_length=1, default="1", verbose_name="Этап запоминания"
    )

    # Communication with the user - specify the user model from the settings so as not to be strictly bound
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Link to a word from the main word model
    core_words = models.ForeignKey(WordsCard, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Накопитель слов"
        verbose_name_plural = "Накопитель слов"
