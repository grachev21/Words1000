from django.urls import path
from users.views import RegisterUser, LoginUser, logout_user
from game.views import Game


urlpatterns = [
    path("game/", Game.as_view(), name="game"),
]