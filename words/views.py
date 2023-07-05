from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import WordsCard
from .models import IntroductionWords
from .models import Word_Accumulator
from .models import SettingsWordNumber
from .models import WordsToRepead
from .models import WordReadingPractice

from .forms import WordCheck
from .forms import AddWordAccumulator
from .forms import WordCountForm
from .forms import ResettingDictionariesForm

from .templatetags.TagWords import menu
from .separate_logic import play_on_words
from .separate_logic.views_logic import DataMixin
from .separate_logic.views_logic import SaveWord
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


def result(request):

    # Форма с результатом статуса
    form_result = AddWordAccumulator(request.POST)
    # Создается контекст
    context = {'response': '', 'form': form_result}
    # Проверяет правильное ли выбранное слова, если правильно добавляет
    # его в context
    if list(request.POST.values())[1] == words['correct_word'][0]:
        context['response'] = 'Правильно'
        # Так же обновляет в базе для чтения слов
        SaveWord(words).save()
    else:
        context['response'] = 'Вы ошиблись'
    # Проверка валидности формы
    if request.method == 'POST':
        if form_result.is_valid():
            dict_set = list(request.POST.keys())
            # Если ответ не равен 0 и запрос status существует,
            # сохраняем в БД.
            if dict_set[1] == 'status' and \
                    str(form_result.cleaned_data['status']) == 'ok':
                db = WordsToRepead.objects.get(word=words['correct_word'][0])
                db.delete()

                # Сохраняем слова в накопитель
                word_arg = words['correct_word'][0]
                form_arg = form_result.cleaned_data['status']
                dbAccum = Word_Accumulator(word=word_arg, word_status=form_arg)
                dbAccum.save()
            return redirect('reading_sentences')

    return render(request, 'words/result.html', context=context)


class LearnNewWords(FormView):
    '''Учить новые слова'''

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


# class Result(FormView):
#     template_name = 'words/result.html'
#     form_class = AddWordAccumulator

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['title'] = 'Результат'
#         return context

#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data()

#         # Форма с результатом статуса
#         form_result = AddWordAccumulator(request.POST)

#         # Проверяет правильное ли выбранное слова
#         if list(request.POST.values())[1] == words['correct_word'][0]:

#             context['response'] = 'Правильно'

#             if WordReadingPractice.objects.exists():
#                 WordReadingPractice.objects.all().delete()
#             WRP = WordReadingPractice(word=words['correct_word'][0])
#             WRP.save()
#         else:
#             context['response'] = 'Вы ошиблись'

#         if request.method == 'POST':
#             if form_result.is_valid():
#                 dict_set = list(request.POST.keys())
#                 # Если ответ не равен 0 и запрос status существует,
#                 # сохраняем в БД.
#                 if dict_set[1] == 'status' and \
#                         str(form_result.cleaned_data['status']) == 'ok':
#                     db = WordsToRepead.objects.get(word=words['correct_word'][0])
#                     db.delete()

#                     # Сохраняем в слова накопитель
#                     word_arg = words['correct_word'][0]
#                     form_arg = form_result.cleaned_data['status']
#                     dbAccum = Word_Accumulator(word=word_arg, word_status=form_arg)
#                     dbAccum.save()
#                 return redirect('reading_sentences')


class ReadingSentences(LearnNewWords, TemplateView):
    '''Читать предложения с угаданном словом'''

    template_name = 'words/reading_sentences.html'

    def init_word(self):
        word = WordReadingPractice.objects.first()
        db = WordsCard.objects.get(word_en=word.word)
        phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)
        if not WordsToRepead.objects.exists():
            return redirect('finish')
        return phrases_set

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тесты'
        context['phrases_set'] = self.init_word()
        return context


# Страница с поздравлением
def finish(request):
    '''Последняя страница'''
    # Возвращает последнюю запись или none
    db = SettingsWordNumber.objects.last()
    words_card = WordsCard.objects.count()
    word_accumulator = Word_Accumulator.objects.count()
    number_to_finish = words_card - word_accumulator

    context = {'title': 'Финиш',
               'db': db,
               'number_to_finish': number_to_finish}

    return render(request, 'words/finish.html', context=context)


def revise_learned(request):
    context = {'title': 'Повторить выучинные сегодня',
               'select': menu[3]['title']}
    return render(request, 'words/revise_learned.html', context=context)


def out(request):
    context = {'title': 'Выход',
               'select': menu[5]['title']}
    return render(request, 'words/out.html', context=context)


class SettingsPage(FormView):
    template_name = 'words/settings.html'
    form_class = WordCountForm

    def get_context_data(self, *args, **kwargs):
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


class ResettingDictionaries(FormView):
    '''Сброс настроек словаря'''
    template_name = 'words/resetting_dictionaries.html'
    form_class = ResettingDictionariesForm

    def get_context_data(self, request, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Сброс словаря'
        print(request)
        return context

    def post(self, request, *args, **kwargs):
        form = ResettingDictionariesForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                if form.cleaned_data['status'] \
                        and form.cleaned_data['yes'] == 'да':

                    Word_Accumulator.objects.all().delete()
                    WordsToRepead.objects.all().delete()
                    IntroductionWords.objects.all().delete()
                    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')
