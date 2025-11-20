from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from mixins.htmx_mixin import HtmxMixin
from settings.forms import ResettingDictionariesForm, WordCountForm
from settings.models import WordsSettings
from settings.services import SettingsMixin


class SettingsPage(HtmxMixin, SettingsMixin, LoginRequiredMixin, FormView):
    # Можно не указывать модель, так как указан form_class
    # model = WordsSettings
    template_name = "include_block.html"
    partial_template_name = "settings/settings.html"
    form_class = WordCountForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")

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
        # Удаляем существующие настройки
        WordsSettings.objects.filter(user=self.request.user).delete()

        # Создаем новые настройки
        WordsSettings.objects.create(
            user=self.request.user,
            number_words=form.cleaned_data["number_words"],
            number_repetitions=form.cleaned_data["number_repetitions"],
            translation_list=form.cleaned_data["translation_list"],
        )

        self.installation_status(user=self.request.user)

        return redirect(self.success_url)


class ResettingDictionaries(HtmxMixin, SettingsMixin, LoginRequiredMixin, FormView):
    template_name = "include_block.html"
    partial_template_name = "settings/resetting_dictionaries.html"
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
