from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import WordsCard


menu = ['Главная',
        'Учить навые слова',
        'Повторить выученные сегодня',
        'Повторить последние 50',
        'Выход']


def home(request):
    words = WordsCard.objects.all()
    context = {
            'menu': menu,
            'words': words,
            'title': 'Words1000'
            }
    return render(request, 'words/home.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')
