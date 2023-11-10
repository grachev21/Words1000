import random
from ..models import WordsCard
from ..models import Word_Accumulator
from ..models import SettingsWordNumber
from ..models import WordsToRepeat

menu = [{'title': 'Читаь слова', 'url_name': 'introduction_words'},
        {'title': 'Учить слова', 'url_name': 'learn_new_words'},
        {'title': 'Повторить', 'url_name': 'revise_learned'},
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
            context['total_words'] = int(WordsCard.objects.count()) - int(Word_Accumulator.objects.count())
            context['counter_word'] = WordsToRepeat.objects.count()
            context['number'] = SettingsWordNumber.objects.first()
            context['total'] = Word_Accumulator.objects.count()
            context['words_counter_home'] = [''] * (WordsCard.objects.count() - Word_Accumulator.objects.count())
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
        

class ReviseLearnedMixin:

    def create_variables_word_accum(self, **kwargs):
        '''Возвращает обхект с тем словом у которого самое малое число повторений'''
        # Получаем статуч того слова у которого самое малое число повторений
        w_a_min = min([words.status for words in Word_Accumulator.objects.select_related('user').filter(user=kwargs['user'])])
        # Получаем список статусов всех слов
        w_a_status = [words.status for words in Word_Accumulator.objects.select_related('user').filter(user=kwargs['user'])]
        # Получаем индекс нужного слова 
        w_a_index = w_a_status.index(w_a_min)
        # Получаем по индексу нужное слова 
        w_a_object = [words for words in Word_Accumulator.objects.select_related('user').filter(user=kwargs['user'])]
        word = w_a_object[w_a_index]
        self.word = word
        return word

    def random_words(self, **kwargs):
        list_without_word = random.sample([w.word_en for w in WordsCard.objects.all() if w.word_en != self.word.word_en], 3)
        list_without_word.append(self.word.word_en)
        return random.sample(list_without_word, 4)