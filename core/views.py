from django.views.generic import ListView, TemplateView, CreateView
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.sites.shortcuts import get_current_site
from core.services.views_logic import DataMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.services import play_on_words
from core.services import str_to_list
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from core.token import account_activation_token
from django.core.mail import EmailMessage
from .models import (WordsCard, WordsConfigJson,
                     IntroductionWords, Word_Accumulator,
                     SettingsWordNumber, WordsToRepeat, RepeatNumber)
from .forms import (WordCheck, LoginUserForm, RegisterUserForm,
                    WordCountForm, ResettingDictionariesForm,
                    AddWordAccumulator)
import random


class Home(DataMixin, ListView):
    model = WordsCard
    template_name = "home.html"
    context_object_name = "words_counter_home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        var = self.list_variables(title="Words1000", user=self.request.user)
        self.logics()
        context["user"] = self.request.user
        context["spinner_data"] = self.word_dict()
        return dict(list(context.items()) + list(var.items()))

    def word_dict(self):
        send_dict = {}
        out_list = []
        list_for_spinner_word_en = [
            data.word_en for data in WordsCard.objects.all()]
        list_for_spinner_word_ru = [
            data.word_ru for data in WordsCard.objects.all()]
        number = [n for n in range(1000)]
        number = random.sample(number, 10)
        word_en = [list_for_spinner_word_en[n] for n in number]
        word_ru = [list_for_spinner_word_ru[n] for n in number]
        for val in range(10):
            send_dict["en"] = word_en[val]
            send_dict["ru"] = word_ru[val]
            out_list.append(dict(send_dict))
        return out_list


class IntroductionWordsList(DataMixin, LoginRequiredMixin, TemplateView):

    template_name = "introduction_words.html"
    login_url = reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["words_card"] = WordsCard.objects.all()
        context["user_model_check"] = self.request.user
        self.save_word_data()
        context["db"] = IntroductionWords \
            .objects.select_related("user").filter(user=self.request.user)

        if self.request.user.is_authenticated:
            context["user_check"] = "on"
        else:
            context["user_check"] = "off"
        var = self.list_variables(
            title="Знакомство",  user=self.request.user
        )
        return dict(list(context.items()) + list(var.items()))

    def save_word_data(self):
        WORD_DATA = play_on_words.main(self.request.user)
        WordsConfigJson.objects.select_related("user").update_or_create(
            WORD_DATA=WORD_DATA, user=self.request.user
        )
        return WORD_DATA


class LearnNewWords(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'learn_new_words.html'
    form_class = WordCheck
    # Переведет на другую страницу не авторизованных пользователей
    login_url = reverse_lazy('register')
    success_url = reverse_lazy('learn_new_words')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        check = Word_Accumulator.objects.select_related(
            'user').filter(user=self.request.user).count()
        if check == 1000:
            context['check_finish'] = 'finish'
            var = self.list_variables(title='Финиш',  user=self.request.user)
            return dict(list(context.items()) + list(var.items()))
        else:
            context['words'] = play_on_words.main(self.request.user)
            WordsConfigJson.objects.select_related('user').filter(
                user=self.request.user).all().delete()
            self.update(context)
            context['user'] = self.request.user
            var = self.list_variables(
                title='Учить новые слова',  user=self.request.user)
            return dict(list(context.items()) + list(var.items()))

    def update(self, context):
        data = {'WORD_DATA': context['words']}
        WordsConfigJson.objects.select_related('user').update_or_create(
            defaults=data, user=self.request.user)

    def post(self, request, **kwargs):
        data = {'WORD_USER': list(request.POST)[-1]}
        WordsConfigJson.objects.select_related('user').update_or_create(
            defaults=data, user=self.request.user)
        return redirect('result')


class ReadingSentences(DataMixin, LoginRequiredMixin, TemplateView):
    template_name = 'reading_sentences.html'
    login_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тесты'
        context['result_word'] = WordsConfigJson.objects.select_related(
            'user').get(user=self.request.user).WORD_USER
        context['phrases_set'], context = self.init_word(context)
        context['word_ru'] = WordsConfigJson.objects.select_related(
            'user').get(user=self.request.user).WORD_DATA
        print(context['phrases_set'])
        context['words_count'] = SettingsWordNumber.objects.select_related(
            'user').get(user=self.request.user).number_words

        val = self.list_variables(title='Тесты', user=self.request.user)
        return dict(list(context.items()) + list(val.items()))

    def init_word(self, context):
        word = WordsConfigJson.objects.select_related(
            'user').get(user=self.request.user).WORD_USER
        db = WordsCard.objects.get(word_en=word)
        phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)
        check = WordsToRepeat.objects.select_related(
            'user').filter(user=self.request.user).count()
        if check == 0:
            context['check_congratulation'] = 'off'
        else:
            context['check_congratulation'] = 'on'
        return phrases_set, context


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        val = self.list_variables(title='Авторизация', user=self.request.user)
        return dict(list(context.items()) + list(val.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Ссылка для активации была отправлена \
            на ваш адрес электронной почты.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse(
                'Пожалуйста зайдите на вашу почту и пройдите по ссылке'
            )
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse(
            'Спасибо за регистрацию, теперь вы можете зайти на сайт.'
        )
    else:
        return HttpResponse('Activation link is invalid!')


def logout_user(request):
    logout(request)
    return redirect('login')


class Result(DataMixin, LoginRequiredMixin, CreateView):

    '''
    Класс обработки формы.
    Метод user_filter получает две переменные WORD_DATA, WORD_USER
    '''
    form_class = AddWordAccumulator
    template_name = 'result.html'
    success_url = reverse_lazy('reading_sentences')
    login_url = reverse_lazy('register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результат'
        # Получаем слова на русском
        word_ru = WordsConfigJson.objects.select_related(
            'user').get(user=self.request.user).WORD_DATA
        # Оставляем только первое слово
        word_ru = word_ru['translate_ru'].split(',')
        context['word_ru'] = word_ru[0]
        context['user'] = self.request.user
        self.user_filter(context)
        var = self.list_variables(title='Результат',  user=self.request.user)
        return dict(list(context.items()) + list(var.items()))

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user
        initial['status'] = '0'
        return initial

    def user_filter(self, context):
        data = WordsConfigJson.objects.select_related(
            'user').get(user=self.request.user)
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
            WordsToRepeat.objects.select_related('user').filter(
                word=word_user, user=self.request.user)\
                .update(repeat_number=num)

        word_user = WordsConfigJson.objects.select_related(
            'user').get(user=self.request.user).WORD_USER
        check = WordsToRepeat.objects.select_related(
            'user').get(user=self.request.user, word=word_user)
        if str(check.repeat_number) == 'one':
            update_db(2)
            return redirect('learn_new_words')
        if str(check.repeat_number) == 'two':
            update_db(3)
            return redirect('learn_new_words')
        if str(check.repeat_number) == 'tree':
            # Удаляем угаданное слова из дневной базы слов
            WordsToRepeat.objects.select_related('user').get(
                user=self.request.user, word=word_user).delete()
            return super().form_valid(form)


class SettingsPage(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'settings.html'
    form_class = WordCountForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        var = self.list_variables(
            title='Настройки',  user=self.request.user)
        return dict(list(context.items()) + list(var.items()))

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        WordsToRepeat.objects.select_related(
            'user').filter(user=self.request.user).delete()
        WordsConfigJson.objects.select_related(
            'user').filter(user=self.request.user).delete()
        SettingsWordNumber.objects.select_related(
            'user').filter(user=self.request.user).delete()
        IntroductionWords.objects.select_related(
            'user').filter(user=self.request.user).delete()
        return super().form_valid(form)


class ResettingDictionaries(LoginRequiredMixin, FormView):
    '''Сбрасывает прогресс словаря пользователя'''

    template_name = 'resetting_dictionaries.html'
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
                status = form.cleaned_data['status']
                yes = form.cleaned_data['yes']
                if status and yes == 'да':
                    Word_Accumulator.objects.select_related(
                        'user').filter(user=self.request.user).delete()
                    WordsToRepeat.objects.select_related(
                        'user').filter(user=self.request.user).delete()
                    IntroductionWords.objects.select_related(
                        'user').filter(user=self.request.user).delete()
                    WordsConfigJson.objects.select_related(
                        'user').filter(user=self.request.user).delete()
                    return redirect('home')
