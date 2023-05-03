from django.urls import path

from words.views import home, learn_new_words, revise_learned_today, repeat_last_50, out

urlpatterns = [
    path('', home, name='home'),
    path('learn_new_words/', learn_new_words, name='learn_new_words'),
    path('revise_learned_today/', revise_learned_today, name='revise_learned_today'),
    path('repeat_last_50/', repeat_last_50, name='repeat_last_50'),
    path('out/', out, name='out'),
]
