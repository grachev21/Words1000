from django.core.exceptions import ValidationError
from django import forms
from .models import SettingsWordNumber
from .models import Word_Accumulator
from .models import Word_status

list_status = ['Удалить весь прогресс', 'hello']

class WordCheck(forms.Form):
    pass


class AddWordAccumulator(forms.ModelForm):

    class Meta:
        model = Word_Accumulator
        fields = ('word', 'word_status')

    def clean_word(self):
        val = self.cleaned_data['word']
        if val != '1234':
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

