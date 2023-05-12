import time
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import redirect

from .models import WordsCard
from .models import WordsToRepead
from .models import SettingsWordNumber
from .models import Word_Accumulator
from .templatetags.TagWords import menu
from .separate_logic.play_on_words import play
from .forms import WordCheck
from .forms import WordCountForm
from .forms import AddWordAccumulator
from .separate_logic import str_to_list



def home(request):

    context = {
            'title': 'Words1000',
            'select': menu[0]['title']
            }
    return render(request, 'words/home.html', context=context)


def result(request):
    form_result  = AddWordAccumulator(request.POST)
    context = {
                'response': '',
                'form': form_result,
                }
    if list(request.POST.values())[1] ==  words['correct_word'][0]:
        context['response'] = 'Правильно'
    else:
        context['response'] = 'Вы ошиблись'

    if request.method == 'POST':
        if form_result.is_valid():

            dict_set = list(request.POST.keys())

            if len(request.POST) != 0 and dict_set[1] == 'status':
                print('-->>', form_result.cleaned_data['status'])
                context['response'] = 'Правильно'
                dbAccum= Word_Accumulator(word=words['correct_word'][0], word_status=form_result.cleaned_data['status'])
                dbAccum.save()

                dbRepead = WordsToRepead(word=words['correct_word'][0])
                dbRepead.save()

                return redirect('reading_sentences')

    return render(request, 'words/result.html', context=context)

def reading_sentences(request):
    db = WordsCard.objects.get(word_en=words['correct_word'][0])

    phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)

    context = {
            'title': 'Тесты с предложениями',
            'db': db,
            'phrases_set': phrases_set,
            }

    return render(request, 'words/reading_sentences.html', context=context)

def learn_new_words(request):
    '''Учить новые слова'''
    form = WordCheck()
    global words
    words = play()
    context = {
            'title': 'Учить новые слова',
            'select': menu[1]['title'],
            'words': words,
            'form': form
            }
    return render(request, 'words/learn_new_words.html', context=context)


def revise_learned_today(request):
    context = {
            'title': 'Повторить выучинные сегодня',
            'select': menu[2]['title']
            }
    return render(request, 'words/revise_learned_today.html', context=context)

def repeat_last_50(request):
    context = {
            'title': 'Повторить последнии 50',
            'select': menu[3]['title']
            }
    return render(request, 'words/repeat_last_50.html', context=context)

def out(request):
    context = {
            'title': 'Выход',
            'select': menu[4]['title']
            }
    return render(request, 'words/out.html', context=context)

def settings(request):
    db = SettingsWordNumber.objects.all()
    db.delete()
    print(request.POST)
    if request.method == 'POST':
        form = WordCountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WordCountForm()

    context = {
            'title': 'Настройки',
            'form': form,
            }

    return render(request, 'words/settings.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')
