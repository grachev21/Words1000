from ..models import WordsCard
from ..models import Word_Accumulator
from ..models import WordsConfigJson


class DataMixin:
    '''Класс примесей'''

    def list_variables(self, **kwargs):
        '''Список переменных'''
        context = kwargs
        # Количество слов из основной
        self.words = WordsCard.objects.count()
        # Количество слов из базы накопления
        self.accum = Word_Accumulator.objects.count()
        # Количество выученных слов
        self.counter = self.words - self.accum
        self.words_counter_home = [''] * self.counter
        # 1000 точек
        context['words_counter_home'] = self.words_counter_home
        context['counter'] = self.counter
        if self.request.user.is_authenticated:
            context['line_off_on'] = 'on'
        else:
            context['line_off_on'] = 'off'
        return context

    def logics(self):
        dot = None
        if self.request.user.is_authenticated:
            dot = ' '
        else:
            dot = ''
        for a in range(self.accum):
            self.words_counter_home.append(dot)


class SaveWord:
    def __init__(self, words):
        self.savewords = words

    def save(self):
        if WordsConfigJson.objects.exists():
            WordsConfigJson.objects.all().delete()
        WRP = WordsConfigJson(word=self.savewords['correct_word'][0])
        WRP.save()
