from django.urls import path
from words.views.home import Home
from words.views.introductionWordslist import IntroductionWordsList
from words.views.learnnewwords import LearnNewWords
from words.views.result import Result
from words.views.reviselearned import ReviseLearned
from words.views.settingspage import SettingsPage
from words.views.readingsentences import ReadingSentences
from words.views.settingspage import ResettingDictionaries
from words.views.register_login import RegisterUser
from words.views.register_login import LoginUser
from words.views.register_login import logout_user
from words.views.register_login import activate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('introduction_words/', IntroductionWordsList.as_view(), name='introduction_words'),
    path('learn_new_words/', LearnNewWords.as_view(), name='learn_new_words'),
    path('result/', Result.as_view(), name='result'),
    path('revise_learned/', ReviseLearned.as_view(), name='revise_learned'),
    path('settings/', SettingsPage.as_view(), name='settings'),
    path('reading_sentences/', ReadingSentences.as_view(), name='reading_sentences'),
    path('resetting_dictionaries/', ResettingDictionaries.as_view(), name='resetting_dictionaries'),
    path('register/', RegisterUser, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 
    activate, name='activate'), 
]

