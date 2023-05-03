from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import WordsCard


menu = [
        {'title': 'Главная',
        'url_name': 'home'},

        {'title': 'Учить новые слова',
        'url_name': 'learn_new_words'},

        {'title': 'Повторить выученные сегодня',
        'url_name': 'revise_learned_today'},

        {'title': 'Повторить последние 50',
        'url_name': 'repeat_last_50'},

        {'title': 'Выход',
        'url_name': 'out'}
        ]



def home(request):
    words = WordsCard.objects.all()
    context = {
            'menu': menu,
            'words': words,
            'title': 'Words1000'
            }
    return render(request, 'words/home.html', context=context)

def learn_new_words(request):
    context = {
            'menu': menu,
            'title': 'Учить новые слова'
            }
    return render(request, 'words/learn_new_words.html', context=context)


def revise_learned_today(request):
    context = {
            'menu': menu,
            'title': 'Повторить выучинные сегодня'
            }
    return render(request, 'words/revise_learned_today.html', context=context)

def repeat_last_50(request):
    context = {
            'menu': menu,
            'title': 'Повторить последнии 50'
            }
    return render(request, 'words/repeat_last_50.html', context=context)

def out(request):
    context = {
            'menu': menu,
            'title': 'Выход'
            }
    return render(request, 'words/out.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')
