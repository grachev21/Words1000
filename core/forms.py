from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.views import AuthenticationForm
from django import forms
from settings.models import WordsSettings
from users.models import WordsUser

list_status = ["Удалить весь прогресс", "hello"]


class WordCheck(forms.Form):
    """The form returns the option of pressed button"""

    pass


class AddWordAccumulator(forms.ModelForm):
    word_en = forms.CharField(
        label="Английский",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Напишите слово на английском",
                "class": "user_form_add_word_accum",
            }
        ),
    )
    word_ru = forms.CharField(
        label="Русский",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Напишите слово на русском",
                "class": "user_form_add_word_accum",
            }
        ),
    )
    user = forms.Field(
        disabled=True,
        label="",
        widget=forms.TextInput(attrs={"class": "user_form_label"}),
    )
    status = forms.Field(
        disabled=True,
        label="",
        widget=forms.TextInput(attrs={"class": "user_form_label"}),
    )

    class Meta:
        model = WordsUser
        fields = ("word_en", "word_ru", "user", "status")

    def clean_word_en(self):
        val_en_user = self.cleaned_data["word_en"]
        user_word_en = WordsConfigJson.objects.first().WORD_USER
        if val_en_user != user_word_en:
            raise ValidationError("Слово должно совпадать")
        else:
            return val_en_user

    def clean_word_ru(self):
        val_ru_user = self.cleaned_data["word_ru"]
        user_word_ru = WordsConfigJson.objects.first().WORD_DATA
        user_word_ru = user_word_ru["translate_ru"].split(",")
        if val_ru_user != user_word_ru[0]:
            raise ValidationError("Слово должно совпадать")
        else:
            return val_ru_user


class WordCountForm(forms.ModelForm):

    class Meta:
        model = WordsSettings()
        fields = ("number_words",)
        widgets = {"number_words": forms.TextInput(attrs={"class": "number-words"})}


class ResettingDictionariesForm(forms.Form):
    yes = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": ""}),
        label='Напишите для подтверждения "yes"',
    )
    status = forms.BooleanField(label="Подтвердите сброс прогресса")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Имя пользователя",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Пароль"
    )
