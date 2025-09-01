from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from game.forms import WordCheck
from game.services import GameInitMixin
from users.models import WordsUser


class Game(GameInitMixin, LoginRequiredMixin, FormView):
    """
    View for playing words.
    And increases the repetition counter for the interval system.
    """

    template_name = "game/game.html"
    form_class = WordCheck
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("game")

    def get_context_data(self, **kwargs):
        """Adds data to initialize the game to context."""
        context = super().get_context_data(**kwargs)
        return self.init_data(user=self.request.user, context=context)

    def post(self, request, *args, **kwargs):
        """
        Makes posts:
        1. If there is Select_DATA - increases the counter -repetition counter
        2. Always delegates the processing of the form to the parental class
        """
        # Word selection processing by user
        if "select_data" in request.POST:
            select_data = request.POST.get("select_data")

            try:
                # We increase the repetition counter for the selected word
                word = WordsUser.objects.get(user=request.user, id=select_data)
                word.number_repetitions += 1
                word.save()
            except WordsUser.DoesNotExist:
                # Ignore if the word is not found (possibly removed)
                pass

        # Standard shape processing
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Redirects to the page of the game after
        successful processing of the form.
        """
        return HttpResponseRedirect(self.get_success_url())
