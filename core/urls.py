from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.Home.as_view(), name="home"),
    path("words/", views.WordsPage.as_view(), name="words"),
]
