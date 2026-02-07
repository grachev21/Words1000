from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from game.forms import WordCheck
from game.services import GameMixin, SettingsMixin, ProgressBarGameMixin
from mixins.htmx_mixin import HtmxMixin
from users.models import WordsUser


class Game(
    GameMixin,
    SettingsMixin,
    ProgressBarGameMixin,
    LoginRequiredMixin,
    HtmxMixin,
    FormView,
):

    # template_name = "components/pages/game/game.html"
    form_class = WordCheck
    template_name = "components/pages/game/game.html"
    partial_template_name = "components/pages/game/game-container.html"
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Word selection processing by user
        if "select_data" in self.request.POST:
            select_data = self.request.POST.get("select_data")

            # Increase the repetition counter for the selected word
            word = WordsUser.objects.get(user=self.request.user, core_words=select_data)
            word.number_repetitions += 1
            word.save()

        # Standard redirect after successful form processing
        return HttpResponseRedirect(self.get_success_url())
