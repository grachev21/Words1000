from django.urls import path
from words.views import revise_learned
from words.views import out
from words.views import home
from words.views import learn_new_words
from words.views import result
from words.views import settings
from words.views import reading_sentences
from words.views import introduction_words
from words.views import finish
from words.views import resetting_dictionaries

urlpatterns = [
    path('', home, name='home'),
    # path('', Home.as_view(), name='home'),
    path('introduction_words/', introduction_words, name='introduction_words'),
    path('learn_new_words/', learn_new_words, name='learn_new_words'),
    path('result/', result, name='result'),
    path('revise_learned/', revise_learned, name='revise_learned'),
    path('out/', out, name='out'),
    path('settings/', settings, name='settings'),
    path('reading_sentences/', reading_sentences, name='reading_sentences'),
    path('finish/', finish, name='finish'),
    path('resetting_dictionaries/', resetting_dictionaries, name='resetting_dictionaries')
]
