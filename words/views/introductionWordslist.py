from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import menu, DataMixin
from ..separate_logic import play_on_words 


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
        print(menu[0]['url_name'])
        return dict(list(context.items()) + list(var.items()))

    def save_word_data(self):
        WORD_DATA = play_on_words.main(self.request.user)
        WordsConfigJson.objects.select_related('user').update_or_create(WORD_DATA=WORD_DATA, user=self.request.user)
        return WORD_DATA
