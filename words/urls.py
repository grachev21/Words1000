from django.urls import path
from words.views import WordsPage


urlpatterns = [path("words/", WordsPage.as_view(), name="words")]
