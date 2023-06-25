from ..models import *

class DataMixin:
    def list_variables(self, **kwargs):
        context = kwargs
        self.words = WordsCard.objects.count()
        self.accum = Word_Accumulator.objects.count()
        self.counter = self.words - self.accum
        self.words_counter_home = ['']* self.counter
        print(context)

    def logics(self):
        for a in range(self.accum):
            self.words_counter_home.append(' ')

