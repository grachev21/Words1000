from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from game.forms import WordCheck
from django.urls import reverse_lazy
from game.services import GameInitMixin
from django.shortcuts import render, redirect
from users.models import WordsUser

class Game(GameInitMixin, LoginRequiredMixin, FormView):
    template_name = "game/game.html"
    form_class = WordCheck
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("game")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Вызываем метод init_data из миксина
        return self.init_data(user=self.request.user, context=context)


    def post(self, request, *args, **kwargs):
        if "select_data" in request.POST:
            select_data = request.POST.get("select_data")

            obj = WordsUser.objects.filter(user=request.user).get(id=select_data)
            obj.number_repetitions += 1
            obj.save()

            return redirect("game")
