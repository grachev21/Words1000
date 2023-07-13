from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.views import AuthenticationForm
from django import forms
from .models import SettingsWordNumber
from .models import Word_Accumulator
# from .models import Word_status
from .models import WordsConfigJson

list_status = ['Удалить весь прогресс', 'hello']

class WordCheck(forms.Form):
    '''
    Форма возвращает вариант нажотой кнопки
    '''
    pass


class AddWordAccumulator(forms.ModelForm):

    class Meta:
        model = Word_Accumulator
        fields = ('word', 'word_status')

    def clean_word(self):
        val = self.cleaned_data['word']
        user_word = WordsConfigJson.objects.first().WORD_USER
        if val != user_word:
            raise ValidationError('Слово должно совпадать')
        else:
            return val


class WordCountForm(forms.ModelForm):

    class Meta:
        model = SettingsWordNumber
        fields = ('number_words',)
        widgets = {
                'number_words': forms.TextInput(attrs={'class': 'number-words'})
                }

class ResettingDictionariesForm(forms.Form):
    yes = forms.CharField(max_length=2, label='Напишите для подтверждения "да"')
    status = forms.BooleanField(label='Подтвердите сброс прогресса')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))