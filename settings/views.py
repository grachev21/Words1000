# Import necessary Django modules and classes
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin to require user authentication
from django.views.generic import CreateView, FormView  # Generic class-based view for creating objects
from django.urls import reverse_lazy  # For lazy URL reversal
from settings.forms import WordCountForm, ResettingDictionariesForm  # Custom form for word count settings
from settings.models import WordsSettings  # Model for storing word settings
from users.models import WordsUser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from core.models import WordsCard
import random

class SettingsPage(LoginRequiredMixin, CreateView):
    template_name = "settings/settings.html"
    form_class = WordCountForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("register")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Настройки"
        return context

    def form_valid(self, form):
        WordsSettings.objects.filter(user=self.request.user).delete()
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ResettingDictionaries(LoginRequiredMixin, FormView):
    template_name = "settings/resetting_dictionaries.html"
    form_class = ResettingDictionariesForm
    login_url = reverse_lazy("register")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Сброс словаря"
        return context

    def post(self, request):
        form = ResettingDictionariesForm(request.POST)
        number_words = WordsSettings.objects.filter(user=self.request.user).last().number_words
        if request.method == "POST":
            if form.is_valid():
                status = form.cleaned_data["status"]
                yes = form.cleaned_data["yes"]
                if status and yes == "yes":
                    # We delete all words
                    WordsUser.objects.filter(user=self.request.user).delete()

                    # We create new words
                    random_elements = random.sample(list(WordsCard.objects.all()), 1000)
                    for element in random_elements:
                        print("record ...")
                        WordsUser.objects.create(user=request.user, core_words=element)

                    # Install status
                    out_words = random.sample(list(WordsUser.objects.filter(user=request.user).all()), number_words)
                    for obj in out_words:
                        obj.status = "2"
                        obj.save()

                    return HttpResponseRedirect(reverse("home"))  

