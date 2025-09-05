from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from settings.forms import WordCountForm, ResettingDictionariesForm
from settings.models import WordsSettings
from settings.services import SettingsMixin


class SettingsPage(SettingsMixin, LoginRequiredMixin, CreateView):
    template_name = "settings/settings.html"
    form_class = WordCountForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("register")

    # The get_form_kwargs method transmits to the user form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    # This method conveys the context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Настройки"
        return context

    def form_valid(self, form):

        if len(WordsSettings.objects.filter(user=self.request.user)) > 1:
            WordsSettings.objects.filter(user=self.request.user).delete()
        WordsSettings.objects.update_or_create(
            user=self.request.user,  # Критерий поиска
            defaults=form.cleaned_data  # Данные для обновления/создания
        )
        self.installation_status(user=self.request.user)

        return super().form_valid(form)


class ResettingDictionaries(SettingsMixin, LoginRequiredMixin, FormView):
    template_name = "settings/resetting_dictionaries.html"
    form_class = ResettingDictionariesForm
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Сброс словаря"
        return context

    def form_valid(self, form):
        # mixins method
        self.delite_list_words(form=form, user=self.request.user)
        self.get_random_list(user=self.request.user)
        self.installation_status(user=self.request.user)

        return super().form_valid(form)
