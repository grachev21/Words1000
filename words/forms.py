from django import forms
from .models import SettingsWordNumber
from .models import Word_Accumulator
from .models import Word_status


class WordCheck(forms.Form):
    pass

class AddWordAccumulator(forms.Form):
    status = forms.ModelChoiceField(queryset=Word_status.objects.all(), label='Категории', empty_label='Не выбрано')

class WordCountForm(forms.ModelForm):

    class Meta:
        model = SettingsWordNumber
        fields = ('number_words',)




