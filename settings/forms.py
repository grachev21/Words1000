from django import forms

from settings.models import WordsSettings


class WordCountForm(forms.ModelForm):
    """
    Form for configuring word count settings for a specific user.
    Fields are populated from the WordsSettings model.
    """

    class Meta:
        model = WordsSettings
        fields = (
            "number_words",
            "number_repetitions",
            "number_write",
            "max_number_read",
            "translation_list",
        )

    def __init__(self, *args, **kwargs):
        # Extract the user from keyword arguments, if provided
        # ← Сохраняем пользователя как атрибут
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # If no user is passed, skip initialization of field values
        if not self.user:
            return

        # Retrieve the user's settings from the database
        user_settings = WordsSettings.objects.filter(user=self.user).first()
        if user_settings:
            self._initialize_fields(user_settings)

    def _initialize_fields(self, settings):
        """
        Set initial values for form fields based on user's saved settings.
        """
        self.fields["number_words"].initial = settings.number_words
        self.fields["number_repetitions"].initial = settings.number_repetitions
        self.fields["translation_list"].initial = settings.translation_list

    def save(self, commit=True):
        """
        Save the form with the user.
        """
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user  # ← Устанавливаем пользователя

        if commit:
            instance.save()

        return instance


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
