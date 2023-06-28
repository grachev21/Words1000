from django.urls import path
from words.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('introduction_words/', IntroductionWords.as_view(), name='introduction_words'),
    path('learn_new_words/', learn_new_words, name='learn_new_words'),
    path('result/', result, name='result'),
    path('revise_learned/', revise_learned, name='revise_learned'),
    path('out/', out, name='out'),
    path('settings/', settings, name='settings'),
    path('reading_sentences/', reading_sentences, name='reading_sentences'),
    path('finish/', finish, name='finish'),
    path('resetting_dictionaries/', resetting_dictionaries, name='resetting_dictionaries')
]
