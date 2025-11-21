from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from game.forms import WordCheck
from game.services import GameInitMixin
from users.models import WordsUser
from mixins.htmx_mixin import HtmxMixin


class Game(HtmxMixin, GameInitMixin, LoginRequiredMixin, FormView):
    """
    View for playing words.
    And increases the repetition counter for the interval system.
    """

    template_name = "include_block.html"
    partial_template_name = "game/game.html"
    form_class = WordCheck
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("game")

    def get_context_data(self, **kwargs):
        """Adds data to initialize the game to context."""
        context = super().get_context_data(**kwargs)
        return self.init_data(user=self.request.user, context=context)

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
            word = WordsUser.objects.get(
                user=self.request.user, core_words=select_data
            )
            word.number_repetitions += 1
            word.save()

        # Standard redirect after successful form processing
        return HttpResponseRedirect(self.get_success_url())
