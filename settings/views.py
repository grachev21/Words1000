from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from settings.forms import WordCountForm, ResettingDictionariesForm
from settings.models import WordsSettings
from settings.services import SettingsMixin
from users.models import WordsUser
from core.models import WordsCard
import random


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
        try:
            with transaction.atomic():
                # Обновляем существующую запись или создаем новую
                WordsSettings.objects.update_or_create(
                    user=self.request.user,
                    defaults=form.cleaned_data
                )

            self.change_list_words(self.request.user)
            return super().form_valid(form)
        except Exception as e:
            print(f"Error {self.request.user}: {e}")
            return self.form_invalid(form)


class ResettingDictionaries(LoginRequiredMixin, FormView):
    template_name = "settings/resetting_dictionaries.html"
    form_class = ResettingDictionariesForm
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Сброс словаря"
        return context

    def form_valid(self, form):
        # Checking the form
        if form.cleaned_data["status"] and form.cleaned_data["yes"] == "yes":
            # We get the number of words from the user settings WordsSettings
            number_words = (
                WordsSettings.objects.filter(user=self.request.user)
                .last()
                .number_words
            )
            # We delete all user words
            WordsUser.objects.filter(user=self.request.user).delete()

            # We create new random words
            random_elements = random.sample(
                list(WordsCard.objects.all()), 1000
            )
            for element in random_elements:
                print("random elements", element)
                WordsUser.objects.create(
                    user=self.request.user, core_words=element
                )

            # Устанавливаем статус для выбранных слов
            out_words = random.sample(
                list(WordsUser.objects.filter(user=self.request.user).all()),
                number_words,
            )
            for obj in out_words:
                print("record")
                obj.status = "2"
                obj.save()

        return super().form_valid(form)
