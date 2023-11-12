from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth.views import AuthenticationForm
from django import forms
from .models import SettingsWordNumber
from .models import Word_Accumulator
from .models import WordsConfigJson

list_status = ['Удалить весь прогресс', 'hello']

class WordCheck(forms.Form):
    '''
    Форма возвращает вариант нажотой кнопки
    '''
    pass

class AddWordAccumulator(forms.ModelForm):
    word_en = forms.CharField(label='Английский', widget=forms.TextInput(attrs={'placeholder': 'Напишите слово на английском', 'class':'user_form_add_word_accum'}))
    word_ru = forms.CharField(label='Русский', widget=forms.TextInput(attrs={'placeholder': 'Напишите слово на русском', 'class':'user_form_add_word_accum'}))
    user = forms.Field(disabled=True, label='', widget=forms.TextInput(attrs={'class': 'user_form_label'}))
    status = forms.Field(disabled=True, label='', widget=forms.TextInput(attrs={'class': 'user_form_label'}))
    class Meta:
        model = Word_Accumulator
        fields = ('word_en', 'word_ru', 'user', 'status')
    def clean_word_en(self):
        val_en_user = self.cleaned_data['word_en']
        user_word_en = WordsConfigJson.objects.first().WORD_USER
        if val_en_user != user_word_en:
            raise ValidationError('Слово должно совпадать')
        else:
            return val_en_user
    def clean_word_ru(self):
        val_ru_user = self.cleaned_data['word_ru']
        user_word_ru = WordsConfigJson.objects.first().WORD_DATA
        user_word_ru = user_word_ru['translate_ru'].split(',')
        if val_ru_user != user_word_ru[0]:
            raise ValidationError('Слово должно совпадать')
        else:
            return val_ru_user

class WordCountForm(forms.ModelForm):
    user = forms.Field(disabled=True)
    class Meta:
        model = SettingsWordNumber
        fields = ('number_words', 'user')
        widgets = {'number_words': forms.TextInput(attrs={'class': 'number-words'})}

class ResettingDictionariesForm(forms.Form):
    yes = forms.CharField(max_length=2, label='Напишите для подтверждения "да"')
    status = forms.BooleanField(label='Подтвердите сброс прогресса')

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'login_form_input'}), help_text='Логин')
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'login_form_input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'login_form_input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'login_form_input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'login_form_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'login_form_input'}))

class ReviseLearnedForm(forms.Form):
    pass
