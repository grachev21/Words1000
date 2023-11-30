from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import menu, DataMixin

class SettingsPage(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'words/settings.html'
    form_class = WordCountForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('register')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        var = self.list_variables(title='Настройки', select=menu[2]['url_name'], user=self.request.user)
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
