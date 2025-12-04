from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from settings.forms import ResettingDictionariesForm, SettingsForm
from settings.models import WordsSettings
from settings.services import SettingsReset, SettingsStatus


class SettingsView(SettingsStatus, LoginRequiredMixin, FormView):
    # Можно не указывать модель, так как указан form_class
    model = WordsSettings
    form_class = SettingsForm
    template_name = "settings/settings.html"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.setup_settings_status(request.user)

    def get_initial(self):
        # Passes the user's current settings to the form when displayed
        settings = self.model.objects.get(user=self.request.user)
        return {
            "number_words": settings.number_words,
            "number_repetitions": settings.number_repetitions,
            "number_write": settings.number_write,
            "max_number_read": settings.max_number_read,
            "translation_list": settings.translation_list,
        }

    # This method conveys the context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Настройки"
        return context

    def form_valid(self, form):
        """Saving user settings"""
        settings_instance, create = WordsSettings.objects.get_or_create(
            user=self.request.user
        )

        # Обновляем поля
        settings_instance.number_words = form.cleaned_data["number_words"]
        settings_instance.number_repetitions = form.cleaned_data["number_repetitions"]
        settings_instance.number_write = form.cleaned_data["number_write"]
        settings_instance.max_number_read = form.cleaned_data["max_number_read"]
        settings_instance.translation_list = form.cleaned_data["translation_list"]

        settings_instance.save()

        return super().form_valid(form)


class ResettingDictionaries(
    SettingsReset, SettingsStatus, LoginRequiredMixin, FormView
):
    template_name = "settings/resetting_dictionaries.html"
    form_class = ResettingDictionariesForm
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("home")

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.setup_settings_reset(request.user)
        self.setup_settings_status(request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Сброс словаря"
        return context
