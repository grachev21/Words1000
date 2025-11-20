from django.urls import path

from . import views

urlpatterns = [
    path("game/", views.Game.as_view(), name="game"),
]
