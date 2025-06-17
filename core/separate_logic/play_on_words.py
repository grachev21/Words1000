import random
from ..models import *

class Settings:
    '''
    При попадании на страницу, learn_new_words метод number_count_default,
    автоматически устанавливает количество слов за день равный 5, но, при том
    условии если оно было не установленно ранее.
    '''
    def __init__(self, user):
        '''Устанавливает переменную для обращению к user'''
        self.USER = user

    def number_count_default(self):
        '''Устанавливает 5 слов в день если нет записей вообще'''
        if not SettingsWordNumber.objects.select_related('user').filter(user=self.USER).exists():
            SettingsWordNumber.objects.select_related('user').create(number_words=5, user=self.USER)

    def value_number_settings(self):
        '''Возвращает установленное количество слов'''
        return SettingsWordNumber.objects.select_related('user').get(user=self.USER).number_words

class Config:
    def __init__(self, NUMBER_WORDS, USER):
        self.wordscard = []
        self.wordsaccumulator = []
        self.NUMBER_WORDS = NUMBER_WORDS
        self.guessing_list = []
        self.USER = USER

    def get_words(self):
        # Собирает все слова на английском и соханяет их в список wordscard
        for W in WordsCard.objects.all():
            self.wordscard.append(W.word_en)

    def base_check(self):
        # Проверяет есть ли угаданные слова в накопительной модели  
        if Word_Accumulator.objects.select_related('user').filter(user=self.USER).exists():
            # если есть то добавляет их в список wordsaccumulator
            for WA in Word_Accumulator.objects.select_related('user').filter(user=self.USER):
                self.wordsaccumulator.append(WA.word_en)
            # далее удаляет их из списка wordscard 
            for wa in self.wordsaccumulator:
                self.wordscard.remove(wa)

    def replay_base_check(self):
        # Проверяет есть ли слова в модели для повторения
        if not WordsToRepeat.objects.select_related('user').filter(user=self.USER).exists():
            words_add_in_repead = random.sample(self.wordscard, self.NUMBER_WORDS)
            # если нет то заполняем ее словами
            for wor in words_add_in_repead:
                # ставим статус zero и имя пользователя
                num = RepeatNumber.objects.get(pk=1)
                WordsToRepeat.objects.select_related('user').create(word=wor, repeat_number=num, user=self.USER)
            # Далее проверяем если модель для ознакомления со словами не пуста 
            if not IntroductionWords.objects.select_related('user').filter(user=self.USER).exists():
                # то удаляем все записи
                IntroductionWords.objects.select_related('user').filter(user=self.USER).delete()
            # и заполняем данными модель для ознакомления IntroductionWords
            for Word in WordsToRepeat.objects.select_related('user').filter(user=self.USER):
                data_Words = WordsCard.objects.get(word_en=Word.word)
                IntroductionWords.objects.select_related('user').create(
                                        word_en=data_Words.word_en,
                                        transcription=data_Words.transcription,
                                        word_ru=data_Words.word_ru, user=self.USER
                                        )

    def list_creation(self):
        '''Формируем список для отправки его в Run_play'''
        for wr in WordsToRepeat.objects.select_related('user').filter(user=self.USER):
            self.guessing_list.append(wr.word)
        data_set = (self.wordscard, self.guessing_list, self.wordsaccumulator)
        return data_set


class Run_play:
    '''Формирует коллекцию данных для сайта, random_list-случайный список, without_word-
    без правильного слова, correct_word-правильное слово.'''
    def __init__(self, data_set):
        self.data_set = data_set
        self.random_list = []
        self.without_word = []
        self.correct_word = random.sample(self.data_set[1], 1)

    def run_without(self):
        '''Формирует список всех слова без правильного слова'''
        for ds in self.data_set[0]:
            if ds != self.correct_word:
                self.without_word.append(ds)

    def create_list(self):
        '''Формирует wrong_words - три слова без правильного варианта, random_list -
        перемешанные слова'''
        print(self.without_word)
        if len(self.without_word) >= 3:
            self.wrong_words = random.sample(self.without_word, 3)
        else:
            finish_list = []
            for w in WordsCard.objects.all():
                if w.word_en != self.correct_word:
                    finish_list.append(w.word_en)
            self.wrong_words = random.sample(finish_list, 3)


        self.random_list = self.wrong_words + self.correct_word
        self.random_list = random.sample(self.random_list, 4)

    def work_db(self):
        '''Создает перевод'''
        self.translate_ru = WordsCard.objects.get(word_en=self.correct_word[0]).word_ru

    def return_result(self):
        '''Возвращает результат с коллекцией'''
        return_data = {
            'correct_word': self.correct_word, 'wrong_words': self.wrong_words,
            'random_list': self.random_list, 'translate_ru': self.translate_ru
        }
        return return_data

def main(user):

    settings = Settings(user)
    settings.number_count_default()
    NUMBER_WORDS = settings.value_number_settings()

    config = Config(NUMBER_WORDS, user)
    config.get_words()
    config.base_check()
    config.replay_base_check()
    data_set = config.list_creation()

    play = Run_play(data_set)
    play.run_without()
    play.create_list()
    play.work_db()
    return play.return_result()
