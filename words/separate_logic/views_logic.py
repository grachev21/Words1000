import random
from ..models import WordsCard
from ..models import Word_Accumulator
from ..models import SettingsWordNumber
from ..models import WordsToRepeat

menu = [{'title': 'Список слов', 'url_name': 'introduction_words'},
        {'title': 'Учить слова', 'url_name': 'learn_new_words'},
        {'title': 'Настройки', 'url_name': 'settings'}]

class DataMixin:
    '''Класс примесей'''

    def list_variables(self, **kwargs):
        '''Список переменных'''
        context = kwargs
        context['menu'] = menu

        # info_bar
        if self.request.user.is_authenticated:
            # Количество слов из основной
            self.words = WordsCard.objects.count()
            # Количество слов из базы накопления
            self.accum = Word_Accumulator.objects.select_related('user').filter(user=context['user']).count()
            # Количество выученных слов
            self.counter = self.words - self.accum
            self.words_counter_home = [''] * self.counter
            # 1000 точек

            context['total_words'] = int(WordsCard.objects.count()) - int(Word_Accumulator.objects.select_related('user').filter(user=context['user']).count())
            context['counter_word'] = WordsToRepeat.objects.select_related('user').filter(user=context['user']).count()
            context['number'] = SettingsWordNumber.objects.select_related('user').filter(user=context['user']).first()
            context['total'] = Word_Accumulator.objects.select_related('user').filter(user=context['user']).count()
            context['words_counter_home'] = self.words_counter_home
            context['counter'] = self.counter
            context['line_off_on'] = 'on'
        else:
            self.words_counter_home = [''] * (WordsCard.objects.count() - Word_Accumulator.objects.count())

            context['total_words'] = int(WordsCard.objects.count()) - int(Word_Accumulator.objects.count())
            context['counter_word'] = WordsToRepeat.objects.count()
            context['number'] = SettingsWordNumber.objects.first()
            context['total'] = Word_Accumulator.objects.count()
            context['words_counter_home'] = self.words_counter_home
            context['counter'] = WordsCard.objects.count() - Word_Accumulator.objects.count()
            context['line_off_on'] = 'off'

        return context

    def logics(self):
        dot = None
        if self.request.user.is_authenticated:
            dot = ' '
            for a in range(Word_Accumulator.objects.select_related('user').count()):
                self.words_counter_home.append(dot)
        else:
            dot = ''
            for a in range(Word_Accumulator.objects.count()):
                self.words_counter_home.append(dot)

