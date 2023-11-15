from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import DataMixin
from ..separate_logic import str_to_list


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
        print(context['phrases_set'])
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
