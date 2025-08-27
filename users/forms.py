from django.contrib.auth.views import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "input-form"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input-form"}),
    )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "input-form"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "input-form"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input-form"}),
    )
    password2 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input-form"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
