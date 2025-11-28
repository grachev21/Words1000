from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from game.forms import WordCheck
from game.services import GameMixin,  SettingsMixin
from mixins.htmx_mixin import HtmxMixin
from users.models import WordsUser


class Game(HtmxMixin, GameMixin, SettingsMixin, LoginRequiredMixin, FormView):
    """
    View for playing words.
    And increases the repetition counter for the interval system.
    """

    template_name = "include_block.html"
    partial_template_name = "game/game.html"
    form_class = WordCheck
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("game")

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.setup_settings(request.user)
        self.setup_game(request.user)

    def form_valid(self, form):
        """
        Processes form validation:
        1. Handles word selection if present in POST data
        2. Always redirects to success URL
        """

        # Word selection processing by user
        if "select_data" in self.request.POST:
            select_data = self.request.POST.get("select_data")

            # Increase the repetition counter for the selected word
            word = WordsUser.objects.get(user=self.request.user, core_words=select_data)
            word.number_repetitions += 1
            word.save()

        # Standard redirect after successful form processing
        return HttpResponseRedirect(self.get_success_url())
