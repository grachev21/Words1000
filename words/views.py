from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import WordsCard
from .templatetags.TagWords import menu

def home(request):
    print(menu)
    words = WordsCard.objects.all()
    context = {
            'menu': menu,
            'words': words,
            'title': 'Words1000',
            'select': menu[0]['title']
            }
    return render(request, 'words/home.html', context=context)

def learn_new_words(request):
    context = {
            'menu': menu,
            'title': 'Учить новые слова',
            'select': menu[1]['title']
            }
    return render(request, 'words/learn_new_words.html', context=context)


def revise_learned_today(request):
    context = {
            'menu': menu,
            'title': 'Повторить выучинные сегодня',
            'select': menu[2]['title']
            }
    return render(request, 'words/revise_learned_today.html', context=context)

def repeat_last_50(request):
    context = {
            'menu': menu,
            'title': 'Повторить последнии 50',
            'select': menu[3]['title']
            }
    return render(request, 'words/repeat_last_50.html', context=context)

def out(request):
    context = {
            'menu': menu,
            'title': 'Выход',
            'select': menu[4]['title']
            }
    return render(request, 'words/out.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')
