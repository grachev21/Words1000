from words import clue
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import menu, DataMixin
from ..separate_logic import play_on_words


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
            clue.clue_ru_fun(context['words']['translate_ru'].split(',')[0])
            clue.clue_en_fun(context['words']['correct_word'][0])
            clue.clue_index_fun(str(context['words']['random_list'].index(context['words']['correct_word'][0])))
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
