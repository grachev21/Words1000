from django.urls import path
from words.views import home

urlpatterns = [
    path('', home, name='home'),
]
