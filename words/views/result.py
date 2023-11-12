from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import menu, DataMixin


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

