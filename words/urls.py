from django.urls import path
from words.views import revise_learned_today
from words.views import out
from words.views import home
from words.views import learn_new_words
from words.views import result
from words.views import repeat_last_50
from words.views import settings
from words.views import reading_sentences

urlpatterns = [
    path('', home, name='home'),
    path('learn_new_words/', learn_new_words, name='learn_new_words'),
    path('result/', result, name='result'),
    path('revise_learned_today/', revise_learned_today, name='revise_learned_today'),
    path('repeat_last_50/', repeat_last_50, name='repeat_last_50'),
    path('out/', out, name='out'),
    path('settings/', settings, name='settings'),
    path('reading_sentences/', reading_sentences, name='reading_sentences'),
]
