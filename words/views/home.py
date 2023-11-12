import random
from django.views.generic import ListView 
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import DataMixin


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
