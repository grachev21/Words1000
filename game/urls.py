from django.urls import path

from . import views

app_name = "game"

urlpatterns = [
    path("game/", views.Game.as_view(), name="game"),
]
