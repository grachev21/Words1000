from django.db import transaction
# Import necessary Django modules and classes
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)  # Mixin to require user authentication
from django.views.generic import (
    CreateView,
    FormView,
)  # Generic class-based view for creating objects
from django.urls import reverse_lazy  # For lazy URL reversal
from settings.forms import (
    WordCountForm,
    ResettingDictionariesForm,
)  # Custom form for word count settings
from settings.models import WordsSettings  # Model for storing word settings
from users.models import WordsUser
from core.models import WordsCard
import random
import logging


logger = logging.getLogger(__name__)


class SettingsPage(LoginRequiredMixin, CreateView):
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
            # We perform through transaction so that when
            # an error is the request is not completed
            with transaction.atomic():
                # We delete the old data
                WordsSettings.objects.filter(user=self.request.user).delete()
                # Record new data.
                # commit=False does not allow me to write down right away
                self.object = form.save(commit=False)
                self.object.user = self.request.user
                self.object.save()
            return super().form_valid(form)
        except Exception as e:
            # Logue and return the error
            logger.warning(f"Failed to save settings for {
                           self.request.user}: {e}")
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
        # Consent status
        status = form.cleaned_data["status"]
        # Written consent
        yes = form.cleaned_data["yes"]

        # Checking the form
        if status and yes == "yes":
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
