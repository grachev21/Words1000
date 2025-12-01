from django import forms
from django.core.exceptions import ValidationError
from settings.models import WordsSettings

class SettingsForm(forms.ModelForm):
    class Meta:
        model = WordsSettings
        fields = [
            "number_words",
            "number_repetitions",
            "number_write",
            "max_number_read",
            "translation_list",
        ]
        widgets = {
            "number_words": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 5,
                    "max": 100,
                    "step": 1,
                }
            ),
            "number_repetitions": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "number_write": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "step": 1,
                }
            ),
            "max_number_read": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "max": 30,
                    "step": 1,
                }
            ),
            "translation_list": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "number_words": "Количество слов за день",
            "number_repetitions": "Как хорошо вы хотите запомнить слово",
            "number_write": "Количество письменных повторений",
            "max_number_read": "Максимальное количество чтения",
            "translation_list": "Показывать перевод в списке слов",
        }
        help_text = {
            "number_words": "От 5 до 100 слов",
            "max_number_read": "Максимум 30 раз",
        }

        def clean_number_words(self):
            number_words = self.cleanded_data["number_words"]
            if number_words < 5 or number_words > 100:
                raise ValidationError("Количество слов должно сыть от 5 до 100")
            return number_words

        def clean_max_number_read(self):
            max_number_read = self.cleaned_data["max_number_read"]
            if max_number_read > 30:
                raise ValidationError("Максимум количество чтений не может превышать 30")


class ResettingDictionariesForm(forms.Form):
    """
    Form for confirming the reset of dictionary progress.
    Requires user to type 'yes' and check a confirmation box.
    """

    yes = forms.CharField(
        label='Введите "yes" чтобы сбросить все данные словаря',
        widget=forms.TextInput(attrs={"placeholder": "####"}),
    )
    status = forms.BooleanField(label="Подтвердить сброс прогресса")
