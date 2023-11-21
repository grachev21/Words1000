from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import menu, DataMixin
from ..separate_logic.views_logic import ReviseLearnedMixin
from ..separate_logic import str_to_list


class ReviseLearned(LoginRequiredMixin, DataMixin, ReviseLearnedMixin, FormView):
    template_name = 'words/revise_learned.html'
    login_url = reverse_lazy('register')
    form_class = ReviseLearnedForm

    def get_context_data(self, *args, **kwargs ):
        context = super().get_context_data(*args, **kwargs)
        var = self.list_variables(title='Повтор', select=menu[2]['url_name'], user=self.request.user)
        context['check_true_list'] = Word_Accumulator.objects.select_related('user').filter(user=self.request.user).count()
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
