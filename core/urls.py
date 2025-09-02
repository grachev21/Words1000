from django.urls import path
from core.views import Home
from core.views import WordsPage


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("words/", WordsPage.as_view(), name="words")
]
