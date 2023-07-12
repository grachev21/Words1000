from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth import logout

from .models import WordsCard
from .models import IntroductionWords
from .models import Word_Accumulator
from .models import SettingsWordNumber
from .models import WordsToRepead
from .models import WordsConfigJson

from .forms import WordCheck
from .forms import AddWordAccumulator
from .forms import WordCountForm
from .forms import ResettingDictionariesForm
from .forms import RegisterUserForm
from .forms import LoginUserForm

from .templatetags.TagWords import menu
from .separate_logic import play_on_words
from .separate_logic.views_logic import DataMixin
from .separate_logic import str_to_list


class Home(DataMixin, ListView):
    '''
    Отображает главную страницу и отображает 1000 слов в виде зеленых точек,
    красные точки отображают выученные слова.
    '''
    # Ссылка на модель
    model = WordsCard
    # Ссылка на шаблон
    template_name = 'words/home.html'
    # Имя переменной контекста в шаблоне
    context_object_name = 'words_counter_home'

    # Контекст
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Класс примиси
        var = self.list_variables(title='Words1000', select=menu[0]['title'])
        self.logics()
        return dict(list(context.items()) + list(var.items()))


class IntroductionWordsList(DataMixin, ListView):
    '''Знакомство со словами'''
    # Ссылка на модель
    model = IntroductionWords
    # Ссылка на шаблон
    template_name = 'words/introduction_words.html'
    # Имя переменной контекста в шаблоне
    context_object_name = 'db'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words_card'] = WordsCard.objects.all()
        if self.request.user.is_authenticated:
            context['user_check'] = 'on'
        else:
            context['user_check'] = 'off'
        # Класс примиси
        var = self.list_variables(title='Знакомство', select=menu[1]['title'])
        return dict(list(context.items()) + list(var.items()))


class LearnNewWords(LoginRequiredMixin, DataMixin, FormView):
    '''
    Страница для тестирования.

    В методе save_word_data - функция play_on_words возвращает коллекцию с
    данными в виде переменной
    WORD_DATA.

    В методе post мы получаем выбранное пользователем слово и сохраняем его в
    базу.

    Метод save_word_data сохраняет коллекцию WORD_DATA в базу данных
    WordsConfigJson
    '''
    template_name = 'words/learn_new_words.html'
    form_class = WordCheck
    # Переведет на другую страницу не авторизованных пользователей
    login_url = reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        WORD_DATA = self.save_word_data()
        context['words'] = WORD_DATA
        var = self.list_variables(title='Учить новые слова',
                                        select=menu[2]['title'])
        return dict(list(context.items()) + list(var.items()))

    def post(self, request, *args, **kwargs):
        WORD_USER = list(request.POST)[-1]
        if WordsConfigJson.objects.exists():
            WordsConfigJson.objects.update(WORD_USER=WORD_USER)
        else:
            WordsConfigJson.objects.create(WORD_USER=WORD_USER)
        return redirect('result')

    def save_word_data(self):
        WORD_DATA = play_on_words.main()
        if WordsConfigJson.objects.exists():
            WordsConfigJson.objects.update(WORD_DATA=WORD_DATA)
        else:
            WordsConfigJson.objects.create(WORD_DATA=WORD_DATA)
        return WORD_DATA



class Result(LoginRequiredMixin, CreateView):
    '''
    Класс обработки формы.
    Метод user_filter получает две переменные WORD_DATA, WORD_USER
    далее эти две переменные сравниваются
    '''
    form_class = AddWordAccumulator
    template_name = 'words/result.html'
    success_url = reverse_lazy('reading_sentences')
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результат'
        self.user_filter(context)
        return context

    def user_filter(self, context):
        word_data = WordsConfigJson.objects.first()
        WORD_DATA = word_data.WORD_DATA

        word_user = WordsConfigJson.objects.first()
        WORD_USER = word_user.WORD_USER

        print(WORD_DATA['correct_word'][0], '<<<')
        if WORD_DATA['correct_word'][0] == WORD_USER:
            context['response'] = 'Ваш ответ правильный!'
            return redirect('reading_sentences')
        else:
            context['response'] = 'Вы ошиблись'

    def post(self, request, *args, **kwargs):
        # Удаляем угаданное слова из дневной базы слов
        WORD_USER = WordsConfigJson.objects.first().WORD_USER
        db = WordsToRepead.objects.get(word=WORD_USER).delete()
        return super().post(request, *args, **kwargs)


class Register(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'words/mes_reg.html'
    # При успешной регистрации направить сюда
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        val = self.list_variables(title='Регистрация')
        return dict(list(context.items()) + list(val.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'words/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        val = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(val.items()))
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class ReadingSentences(LoginRequiredMixin, TemplateView):
    '''
    Читать словом
    Метод init  получает переменную со словом пользователя и находит это слово в общей базе слов 
    '''

    template_name = 'words/reading_sentences.html'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тесты'
        context['phrases_set'] = self.init_word()
        return context

    def init_word(self):
        word = WordsConfigJson.objects.first().WORD_USER
        db = WordsCard.objects.get(word_en=word)
        phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)
        if not WordsToRepead.objects.exists():
            return redirect('finish')
        return phrases_set


class SettingsPage(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'words/settings.html'
    form_class = WordCountForm
    login_url = reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        var = self.list_variables(title='Настройки', select=menu[4]['title'])
        return dict(list(context.items()) + list(var.items()))

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


class ResettingDictionaries(LoginRequiredMixin, FormView):
    '''Сброс настроек словаря'''
    template_name = 'words/resetting_dictionaries.html'
    form_class = ResettingDictionariesForm
    login_url =  reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Сброс словаря'
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

def out(request):
    context = {'title': 'Выход',
               'select': menu[5]['title']}
    return render(request, 'words/out.html', context=context)


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




def pageNotFound(request, exception):
    return HttpResponseNotFound('Страничка не найдена')




