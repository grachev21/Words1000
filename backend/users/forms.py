from django.contrib.auth.views import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"placeholder": "Имя"}),
    )
    password = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}),
    )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Введите имя",
        widget=forms.TextInput(attrs={"placeholder": "Имя"}),
    )
    email = forms.EmailField(
        label="Введите свой Email",
        widget=forms.EmailInput(attrs={"placeholder": "@"}),
    )
    password1 = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
