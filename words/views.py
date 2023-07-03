from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import Word_status
from .models import WordsCard
from .models import IntroductionWords
from .models import Word_Accumulator
from .models import SettingsWordNumber
from .models import WordsToRepead

from .forms import WordCheck
from .forms import AddWordAccumulator
from .forms import WordCountForm
from .forms import ResettingDictionariesForm

from .templatetags.TagWords import menu
from .separate_logic import play_on_words
from .separate_logic.views_logic import *
from .separate_logic import str_to_list

class Home(DataMixin, ListView):
    '''Домошняя страница'''
    model = WordsCard
    template_name = 'words/home.html'
    context_object_name = 'words_counter_home'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Класс примиси
        var = self.list_variables(title='Words1000', select=menu[0]['title'])
        self.logics()
        return dict(list(context.items()) + list(var.items()))


class IntroductionWordsList(DataMixin, ListView):
    '''Знакомство со словами'''
    model = IntroductionWords
    template_name = 'words/introduction_words.html'
    context_object_name = 'db'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Класс примиси
        var = self.list_variables(title='Знакомство', select=menu[1]['title'])
        return dict(list(context.items()) + list(var.items()))


# Выбераем статус слова 
def result(request):
    # Форма с результатом статуса
    form_result  = AddWordAccumulator(request.POST)
    context = {
                'response': '',
                'form': form_result,
                }
    # Проверяет правильное ли выбранное слова
    if list(request.POST.values())[1] ==  words['correct_word'][0]:
        context['response'] = 'Правильно'
    else:
        context['response'] = 'Вы ошиблись'
    if request.method == 'POST':
        if form_result.is_valid():
            dict_set = list(request.POST.keys())
            # Если ответ не равен 0 и запрос status существует, 
            # сохраняем в БД.
            if dict_set[1] == 'status' and str(form_result.cleaned_data['status']) == 'Знаю':
                db = WordsToRepead.objects.get(word=words['correct_word'][0])
                db.delete()
                # Сохраняем в слова накопитель
                dbAccum = Word_Accumulator(word=words['correct_word'][0],
                          word_status=form_result.cleaned_data['status'])
                dbAccum.save()

            return redirect('reading_sentences')

    return render(request, 'words/result.html', context=context)

# Чтение фраз на английском
def reading_sentences(request):
    db = WordsCard.objects.get(word_en=words['correct_word'][0])

    phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)

    context = {
            'title': 'Тесты с предложениями',
            'db': db,
            'phrases_set': phrases_set,
            }
    if not WordsToRepead.objects.exists():
        return redirect('finish')

    return render(request, 'words/reading_sentences.html', context=context)

def finish(request):
    db = SettingsWordNumber.objects.last()
    words_card = WordsCard.objects.count()
    word_accumulator = Word_Accumulator.objects.count()
    number_to_finish = words_card - word_accumulator
    context = {
            'title': 'Финиш',
            'db': db,
            'number_to_finish': number_to_finish
            }
    return render(request, 'words/finish.html', context=context)

class LearnNewWords(FormView):
    template_name = 'words/learn_new_words.html'
    form_class = WordCheck
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Учить новые слова'
        context['select'] = menu[2]['title']
        global words
        words = play_on_words.main()
        context['words'] = words
        return context


def revise_learned(request):
    context = {
        'title': 'Повторить выучинные сегодня',
        'select': menu[3]['title']
        }
    return render(request, 'words/revise_learned.html', context=context)


def out(request):
    context = {
            'title': 'Выход',
            'select': menu[5]['title']
            }
    print(play_on_words.main())
    return render(request, 'words/out.html', context=context)


class SettingsPage(FormView):
    template_name = 'words/settings.html'
    form_class = WordCountForm

    def get_context_dataa(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Настройки'
        context['select'] = menu[4]['title']
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = WordCountForm(request.POST)
            if form.is_valid():
                data = WordsToRepead.objects.all()
                data.delete()
                db = SettingsWordNumber.objects.all()
                db.delete()
                form.save()
                return redirect('home')
        else:
            form = WordCountForm()


def resetting_dictionaries(request):
    form = ResettingDictionariesForm(request.POST or None)
    context = {
            'title': 'Сброс словаря',
            'form': form
            }

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['status'] == True and form.cleaned_data['yes'] == 'да':

                Word_Accumulator.objects.all().delete()
                WordsToRepead.objects.all().delete()
                IntroductionWords.objects.all().delete()
                return redirect('home')
    return render(request, 'words/resetting_dictionaries.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')
