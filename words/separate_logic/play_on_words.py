import random
from ..models import WordsCard
from ..models import Word_Accumulator
from ..models import SettingsWordNumber
from ..models import WordsToRepead
from ..models import IntroductionWords



def number_count_default():
    '''Устанавливает по умолчанию количество слов (5) по умолчанию'''

    if SettingsWordNumber.objects.exists():
        pass
    else:
        db = SettingsWordNumber(number_words=5)
        db.save()

def value_number_settings():
    '''Возвращает количество слов в настройках'''

    db = SettingsWordNumber.objects.get()
    NUMBER_WORDS = db.number_words
    return NUMBER_WORDS


def config(NUMBER_WORDS):
    '''
1.[x] Получаем все слова из основной базы в список 'wordscard'.

2.[x] Проверяем есть ли слова в накопительной базе, если есть то получаем все
      слова из накопительной базы в список 'wordsaccumulator' и удаляем эти
      слова из списка 'wordscard'.

3.[x] Проверяем есть ли записи в базе для повторения, если нет то из списка
      wordscard, выбираем количество слов равной переменной
      NUMBER_WORDS и сохраняем их в базу для повторения.

4.[x] Создаем список для отгадывания слов 'guessing_list' на основе базы для
      повторения.
    '''

    # 1.
    wordscard = []
    for W in WordsCard.objects.all():
        wordscard.append(W.word_en)

    # 2.
    wordsaccumulator = []
    if Word_Accumulator.objects.exists():

        for WA in Word_Accumulator.objects.all():
            wordsaccumulator.append(WA.word)
        for wa in wordsaccumulator:
            wordscard.remove(wa)

    # 3.
    if WordsToRepead.objects.count() == 0:

        words_add_in_repead = random.sample(wordscard, NUMBER_WORDS)
        for wor in words_add_in_repead:
            db = WordsToRepead(word=wor)
            db.save()

        # Если база для ознакомления не пуста то очищаем ее
        if IntroductionWords.objects.count() != 0:
            Intro = IntroductionWords.objects.all()
            Intro.delete()

        # Заполняем базу для ознакомления 
        for Word in WordsToRepead.objects.all():
            key = WordsCard.objects.get(word_en=Word.word)
            key_pk = key.pk
            data_Words = WordsCard.objects.get(pk=key_pk)
            db_introduction = IntroductionWords(word_en=data_Words.word_en,
                                                transcription= data_Words.transcription,
                                                word_ru=data_Words.word_ru)
            db_introduction.save()



    # 4.
    guessing_list = []
    for wr in WordsToRepead.objects.all():
        guessing_list.append(wr.word)

    data_set = (wordscard, guessing_list, wordsaccumulator)

    return data_set


def run_play(data_set):

    # Конечный список для теста
    random_list = []
    # Список без правильного слова
    without_word = []
    # Выбераем слово которое нужно угадать из списка слов для повторения
    correct_word = random.sample(data_set[1], 1)

    # Перебираем весь словарь 
    for ds in data_set[0]:
        # Если это не то слово которое нужно угадать, то добавляем его в список
        if ds != correct_word:
            without_word.append(ds)

    # Получаем три неправильных слова
    wrong_words = random.sample(without_word, 3)
    # Соединяем правильное слово и не правильные слова
    random_list = wrong_words + correct_word
    # Перемешиваем
    random_list = random.sample(random_list, 4)
    # Получаем перевод на русский
    print(correct_word[0])
    print(len(correct_word[0]))
    db =  WordsCard.objects.get(word_en=correct_word[0])
    translate = WordsCard.objects.get(pk=db.pk)
    translate_ru = translate.word_ru


    return_data = {
            'correct_word': correct_word, # Правильное слово
            'wrong_words': wrong_words,   # Не правильные слова
            'random_list': random_list,   # Смешаный список
            'translate_ru': translate_ru  # На русском
            }

    return return_data


def play():
    '''Главная функция'''

    number_count_default()
    NUMBER_WORDS = value_number_settings()
    data_set = config(NUMBER_WORDS)
    return run_play(data_set)


