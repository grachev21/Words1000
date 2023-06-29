import random
from ..models import *

# Класс настроек
class Settings:
    # Метод устанавливает количество слов 
    def number_count_default(self):
        if not SettingsWordNumber.objects.exists():
            db = SettingsWordNumber(number_words=5)
            db.save()

    def value_number_settings(self):
        db = SettingsWordNumber.objects.get()
        NUMBER_WORDS = db.number_words
        return NUMBER_WORDS

class Config:
    def __init__(self, NUMBER_WORDS):
        self.wordscard = []
        self.wordsaccumulator = []
        self.NUMBER_WORDS = NUMBER_WORDS
        self.guessing_list = []

    def get_words(self):
        for W in WordsCard.objects.all():
            self.wordscard.append(W.word_en)

    def base_check(self):
        if Word_Accumulator.objects.exists():
            for WA in Word_Accumulator.objects.all():
                self.wordsaccumulator.append(WA.word)
            for wa in self.wordsaccumulator:
                self.wordscard.remove(wa)

    def replay_base_check(self):
        if WordsToRepead.objects.count() == 0:
            words_add_in_repead = random.sample(self.wordscard, self.NUMBER_WORDS)
            for wor in words_add_in_repead:
                db = WordsToRepead(word=wor)
                db.save()
            if IntroductionWords.objects.count() != 0:
                Intro = IntroductionWords.objects.all()
                Intro.delete()
            for Word in WordsToRepead.objects.all():
                key = WordsCard.objects.get(word_en=Word.word)
                key_pk = key.pk
                data_Words = WordsCard.objects.get(pk=key_pk)
                db_introduction = IntroductionWords(word_en=data_Words.word_en,
                                                    transcription= data_Words.transcription,
                                                    word_ru=data_Words.word_ru)
                db_introduction.save()

    def list_creation(self):
        for wr in WordsToRepead.objects.all():
            self.guessing_list.append(wr.word)
        data_set = (self.wordscard, self.guessing_list, self.wordsaccumulator)
        return data_set

class Run_play:
    def __init__(self, data_set):
        self.data_set = data_set
        self.random_list = []
        self.without_word = []
        self.correct_word = random.sample(self.data_set[1], 1)

    def run_without(self):
        for ds in self.data_set[0]:
            if ds != self.correct_word:
                self.without_word.append(ds)

    def create_list(self):
        self.wrong_words = random.sample(self.without_word, 3)
        self.random_list = self.wrong_words + self.correct_word
        self.random_list = random.sample(self.random_list, 4)

    def work_db(self):
        db =  WordsCard.objects.get(word_en=self.correct_word[0])
        translate = WordsCard.objects.get(pk=db.pk)
        self.translate_ru = translate.word_ru

    def return_result(self):
        return_data = {
            'correct_word': self.correct_word, 'wrong_words': self.wrong_words,
            'random_list': self.random_list, 'translate_ru': self.translate_ru
        }
        return return_data
