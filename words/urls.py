from django.urls import path
from words.views import Home
from words.views import IntroductionWordsList
from words.views import LearnNewWords
from words.views import Result
from words.views import ReviseLearned
from words.views import out
from words.views import SettingsPage
from words.views import ReadingSentences
from words.views import ResettingDictionaries
from words.views import RegisterUser
from words.views import LoginUser
from words.views import logout_user

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('introduction_words/', IntroductionWordsList.as_view(), name='introduction_words'),
    path('learn_new_words/', LearnNewWords.as_view(), name='learn_new_words'),
    path('result/', Result.as_view(), name='result'),
    path('revise_learned/', ReviseLearned.as_view(), name='revise_learned'),
    path('out/', out, name='out'),
    path('settings/', SettingsPage.as_view(), name='settings'),
    path('reading_sentences/', ReadingSentences.as_view(), name='reading_sentences'),
    path('resetting_dictionaries/', ResettingDictionaries.as_view(), name='resetting_dictionaries'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]