from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import SettingsWordNumber
from .models import Word_Accumulator
from .models import Word_status
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
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пороль')
    password2 = forms.CharField(label='Пороль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



