# Import Django forms module for creating form classes
from django import forms

# Import the WordsSettings model from the settings app
from settings.models import WordsSettings


class WordCountForm(forms.ModelForm):
    class Meta:
        model = WordsSettings
        fields = ("number_words", "number_repetitions", "translation_list")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем пользователя из аргументов
        super().__init__(*args, **kwargs)

        # Если пользователь передан и у него есть настройки, устанавливаем начальные значения
        if user:
            try:
                user_settings = WordsSettings.objects.get(user=user)
                self.fields['number_words'].initial = user_settings.number_words
                self.fields['number_repetitions'].initial = user_settings.number_repetitions
                self.fields['translation_list'].initial = user_settings.translation_list
            except WordsSettings.DoesNotExist:
                pass  # Если настроек нет, оставляем значения по умолчанию

        


class ResettingDictionariesForm(forms.Form):
    yes = forms.CharField(
    widget=forms.TextInput(attrs={"placeholder": ""}),
        label='Напишите для подтверждения "yes"',
    )
    status = forms.BooleanField(label="Подтвердите сброс прогресса")