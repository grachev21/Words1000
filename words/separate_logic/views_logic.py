from ..models import WordsCard
from ..models import Word_Accumulator
from ..models import WordReadingPractice


class DataMixin:
    def list_variables(self, **kwargs):
        context = kwargs
        self.words = WordsCard.objects.count()
        self.accum = Word_Accumulator.objects.count()
        self.counter = self.words - self.accum
        self.words_counter_home = [''] * self.counter
        context['words_counter_home'] = self.words_counter_home
        context['counter'] = self.counter
        return context

    def logics(self):
        for a in range(self.accum):
            self.words_counter_home.append(' ')


class SaveWord:
    '''Сохраняет слово переменной words'''
    def __init__(self, words):
        self.savewords = words

    def save(self):
        if WordReadingPractice.objects.exists():
            WordReadingPractice.objects.all().delete()
        WRP = WordReadingPractice(word=self.savewords['correct_word'][0])
        WRP.save()
