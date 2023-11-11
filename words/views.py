# import clue
import random
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import IntroductionWords
from .models import SettingsWordNumber
from .models import WordsConfigJson
from .models import Word_Accumulator
from .models import WordsToRepeat
from .models import WordsCard
from .models import RepeatNumber
from .forms import LoginUserForm
from .forms import RegisterUserForm
from .forms import ResettingDictionariesForm
from .forms import WordCountForm
from .forms import AddWordAccumulator
from .forms import WordCheck
from .forms import ReviseLearnedForm
from .separate_logic.views_logic import menu, DataMixin
from .separate_logic.views_logic import ReviseLearnedMixin
from .separate_logic import play_on_words, str_to_list


class Home(DataMixin, ListView):
    '''
    Отображает главную страницу и отображает 1000 слов в виде зеленых точек,
    красные точки отображают выученные слова.
    '''
    model = WordsCard
    template_name = 'words/home.html'
    context_object_name = 'words_counter_home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        var = self.list_variables(title='Words1000', user=self.request.user)
        self.logics()
        context['user'] = self.request.user
        context['spinner_data'] = self.word_dict()
        return dict(list(context.items()) + list(var.items()))

    def word_dict(self):
        send_dict = {}
        out_list = []
        list_for_spinner_word_en = [data.word_en for data in WordsCard.objects.all()]
        list_for_spinner_word_ru = [data.word_ru for data in WordsCard.objects.all()]
        number = [n for n in range(1000)]
        number = random.sample(number, 10)
        word_en = [list_for_spinner_word_en[n] for n in number]
        word_ru = [list_for_spinner_word_ru[n] for n in number]
        for val in range(10):
            send_dict['en'] = word_en[val]
            send_dict['ru'] = word_ru[val]
            out_list.append(dict(send_dict))
        return out_list

class IntroductionWordsList(DataMixin, LoginRequiredMixin, TemplateView):
    '''Знакомство со словами'''
    template_name = 'words/introduction_words.html'
    login_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words_card'] = WordsCard.objects.all()
        context['user_model_check'] = self.request.user
        self.save_word_data()
        context['db'] = IntroductionWords.objects.select_related('user').filter(user=self.request.user)
        if self.request.user.is_authenticated:
            context['user_check'] = 'on'
        else:
            context['user_check'] = 'off'
        # Класс примиси
        var = self.list_variables(title='Знакомство', select=menu[0]['url_name'], user=self.request.user)
        return dict(list(context.items()) + list(var.items()))

    def save_word_data(self):
        WORD_DATA = play_on_words.main(self.request.user)
        WordsConfigJson.objects.select_related('user').update_or_create(WORD_DATA=WORD_DATA, user=self.request.user)
        return WORD_DATA


class LearnNewWords(LoginRequiredMixin, DataMixin, FormView):
    '''
    Страница для тестирования.

    В методе save_word_data - функция play_on_words возвращает коллекцию с
    данными в виде переменной
    WORD_DATA.

    В методе post мы получаем выбранное пользователем слово и сохраняем его в
    базу WordsConfigJson.

    Метод save_word_data сохраняет коллекцию WORD_DATA в базу данных
    WordsConfigJson
    '''
    template_name = 'words/learn_new_words.html'
    form_class = WordCheck
    # Переведет на другую страницу не авторизованных пользователей
    login_url = reverse_lazy('register')
    success_url = reverse_lazy('learn_new_words')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if Word_Accumulator.objects.select_related('user').filter(user=self.request.user).count() == 1000:
            context['check_finish'] = 'finish'
            var = self.list_variables(title='Финиш', select=menu[1]['title'], user=self.request.user)
            return dict(list(context.items()) + list(var.items()))
        else:
            context['words'] = play_on_words.main(self.request.user)
            WordsConfigJson.objects.select_related('user').filter(user=self.request.user).all().delete()
            self.update(context)
            context['user'] = self.request.user
            # test
            # clue.clue_ru_fun(context['words']['translate_ru'].split(',')[0])
            # clue.clue_en_fun(context['words']['correct_word'][0])
            # clue.clue_index_fun(str(context['words']['random_list'].index(context['words']['correct_word'][0])))
            # end test
            var = self.list_variables(title='Учить новые слова', select=menu[2]['url_name'], user=self.request.user)
            return dict(list(context.items()) + list(var.items()))
    
    def update(self, context):
        data = {'WORD_DATA': context['words']}
        WordsConfigJson.objects.select_related('user').update_or_create(defaults=data, user=self.request.user)
    def post(self, request, **kwargs):
        data = {'WORD_USER': list(request.POST)[-1]}
        WordsConfigJson.objects.select_related('user').update_or_create(defaults=data, user=self.request.user)
        return redirect('result')

class ReviseLearned(LoginRequiredMixin, DataMixin, ReviseLearnedMixin, FormView):
    template_name = 'words/revise_learned.html'
    login_url = reverse_lazy('register')
    form_class = ReviseLearnedForm

    def get_context_data(self, *args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        var = self.list_variables(title='Повтор', select=menu[2]['url_name'], user=self.request.user)
        # context['check_true_list'] = Word_Accumulator.objects.select_related('user').filter(user=self.request.user).count()
        context['check_true_list'] = 33
        if Word_Accumulator.objects.select_related('user').filter(user=self.request.user).exists():
            context['word_accum_object'] = self.create_variables_word_accum(user=self.request.user)
            context['random_words'] = self.random_words()

        return dict(list(context.items()) + list(var.items()))

    def post(self, request,  **kwargs):
        context = self.get_context_data(**kwargs)
        word = list(request.POST)[-1]
        word_to_accum = self.create_variables_word_accum(user=self.request.user)
        if word_to_accum.word_en == list(request.POST)[-1]:
            context['user_result'] = 'ok'
            context['phrases_set'] = self.init_word(word)
            status_num = context['word_accum_object'].status + 1
            Word_Accumulator.objects.select_related('user').filter(user=self.request.user, word_en=list(request.POST)[-1]).update(status=status_num)
        else:
            context['user_result'] = 'no'
            context['response_result'] = 'Ваш ответ не верный'
            context['word'] = word_to_accum.word_en
        return render(request, self.template_name, context=context)

    def init_word(self, word):
        db = WordsCard.objects.get(word_en=word)
        phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)
        return phrases_set

class Result(DataMixin, LoginRequiredMixin, CreateView):
    '''
    Класс обработки формы.
    Метод user_filter получает две переменные WORD_DATA, WORD_USER
    '''
    form_class = AddWordAccumulator
    template_name = 'words/result.html'
    success_url = reverse_lazy('reading_sentences')
    login_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результат'
        # Получаем слова на русском 
        word_ru = WordsConfigJson.objects.select_related('user').get(user=self.request.user).WORD_DATA
        # Оставляем только первое слово
        word_ru = word_ru['translate_ru'].split(',')
        context['word_ru'] = word_ru[0]
        context['user'] = self.request.user
        self.user_filter(context)
        var = self.list_variables(title='Результат', select=menu[2]['url_name'], user=self.request.user)
        return dict(list(context.items()) + list(var.items()))

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user 
        initial['status'] = '0'
        return initial

    def user_filter(self, context):
        data = WordsConfigJson.objects.select_related('user').get(user=self.request.user)
        context['correct_word'] = data.WORD_DATA['correct_word'][0]
        # print(data.WORD_USER)
        # print(data.WORD_DATA['correct_word'][0])
        if data.WORD_DATA['correct_word'][0] == data.WORD_USER:
            context['response'] = 1
            return redirect('reading_sentences')
        else:
            context['response'] = 0

    def form_valid(self, form):

        def update_db(number):
            num = RepeatNumber.objects.get(pk=number)
            WordsToRepeat.objects.select_related('user').filter(word=word_user, user=self.request.user).update(repeat_number=num)

        word_user = WordsConfigJson.objects.select_related('user').get(user=self.request.user).WORD_USER
        check = WordsToRepeat.objects.select_related('user').get(user=self.request.user, word=word_user)
        if str(check.repeat_number) == 'one':
            update_db(2)
            return redirect('learn_new_words')
        if str(check.repeat_number) == 'two':
            update_db(3)
            return redirect('learn_new_words')
        if str(check.repeat_number) == 'tree':
            # Удаляем угаданное слова из дневной базы слов
            WordsToRepeat.objects.select_related('user').get(user=self.request.user, word=word_user).delete()
            return super().form_valid(form)

# Register =======================================================================
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'words/register.html'
    # При успешной регистрации направить сюда
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        val = self.list_variables(title='Регистрация', user=self.request.user)
        return dict(list(context.items()) + list(val.items()))

    # def post(self, request):
        # pass
        
        
        

# EndRegister ====================================================================
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'words/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        val = self.list_variables(title='Авторизация', user=self.request.user)
        return dict(list(context.items()) + list(val.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class ReadingSentences(DataMixin, LoginRequiredMixin, TemplateView):
    '''
    Читать словом
    Метод init  получает переменную со словом пользователя и находит это слово в общей базе слов
    '''
    template_name = 'words/reading_sentences.html'
    login_url = reverse_lazy('register')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тесты'
        context['result_word'] = WordsConfigJson.objects.select_related('user').get(user=self.request.user).WORD_USER
        context['phrases_set'], context = self.init_word(context)
        context['words_count'] = SettingsWordNumber.objects.select_related('user').get(user=self.request.user).number_words
        val = self.list_variables(title='Тесты', user=self.request.user)
        return dict(list(context.items()) + list(val.items()))
    def init_word(self, context):
        word = WordsConfigJson.objects.select_related('user').get(user=self.request.user).WORD_USER
        db = WordsCard.objects.get(word_en=word)
        phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)
        if WordsToRepeat.objects.select_related('user').filter(user=self.request.user).count() == 0:
            context['check_congratulation'] = 'off'
        else:
            context['check_congratulation'] = 'on'

        return phrases_set, context

class SettingsPage(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'words/settings.html'
    form_class = WordCountForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        var = self.list_variables(title='Настройки', select=menu[3]['url_name'], user=self.request.user)
        return dict(list(context.items()) + list(var.items()))

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        WordsToRepeat.objects.select_related('user').filter(user=self.request.user).delete()
        WordsConfigJson.objects.select_related('user').filter(user=self.request.user).delete()
        SettingsWordNumber.objects.select_related('user').filter(user=self.request.user).delete()
        IntroductionWords.objects.select_related('user').filter(user=self.request.user).delete()
        return super().form_valid(form)

class ResettingDictionaries(LoginRequiredMixin, FormView):
    '''Сбрасывает прогресс словаря пользователя'''

    template_name = 'words/resetting_dictionaries.html'
    form_class = ResettingDictionariesForm
    login_url = reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Сброс словаря'
        return context

    def post(self, request):
        form = ResettingDictionariesForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                if form.cleaned_data['status'] and form.cleaned_data['yes'] == 'да':
                    Word_Accumulator.objects.select_related('user').filter(user=self.request.user).delete()
                    WordsToRepeat.objects.select_related('user').filter(user=self.request.user).delete()
                    IntroductionWords.objects.select_related('user').filter(user=self.request.user).delete()
                    WordsConfigJson.objects.select_related('user').filter(user=self.request.user).delete()
                    return redirect('home')

def out(request):
    context = {'title': 'Выход',
               'select': menu[5]['title']}
    return render(request, 'words/out.html', context=context)


def pageNotFound(request, HttpResponseNotFound):
    return HttpResponseNotFound('Страничка не найдена')
