import random
from ..models import WordsCard
from ..models import Word_Accumulator
from ..models import SettingsWordNumber
from ..models import WordsToRepead



# [1]
def number_count_default():
    if SettingsWordNumber.objects.exists():
        pass
    else:
        db = SettingsWordNumber(number_words=5)
        db.save()

def value_number_settings():
    db = SettingsWordNumber.objects.get()
    NUMBER_WORDS = db.number_words
    return NUMBER_WORDS


# [2]
def config(NUMBER_WORDS):
    '''Создает два временных списка и возвращает их в кортеже
    Далее проверяется есть ли в накапительной таблице слова'''
    wordscard = []
    wordsaccumulator = []

    # Метод exists возвращает истину если таблица не пуста
    count_check = Word_Accumulator.objects.exists()

    # Получаем все слова из базы данных
    for W in WordsCard.objects.all():
        wordscard.append(W.word_en)


    for A in Word_Accumulator.objects.all():
        wordsaccumulator.append(A.word)

    if WordsToRepead.objects.count() == NUMBER_WORDS:
        # Из всех слов выбираем рандомно через переменную NUMBER_WORDS
        print('Вы выучили все слова')


    data_set = (
            count_check,
            wordscard,
            wordsaccumulator,
            )

    return data_set

# [3]
def del_word(data_set):
    '''Удаляет из временного списка слова которые уже отгаданы'''
    for word in data_set[2]:
        data_set[1].remove(word)

# [4]
def run_play(data_set):
    random_list = [] # Конечный список для теста
    without_word = [] # Список без правильного слова
    correct_word = random.sample(data_set[1], 1) # Слово которое нужно угадать

    # Перебираем весь словарь
    for ds in data_set[1]:
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
    translate_ru = WordsCard.objects.get(word_en=correct_word[0])

    return_data = {
            'correct_word': correct_word,
            'wrong_words': wrong_words,
            'random_list': random_list,
            'translate_ru': translate_ru
            }
    return return_data


def play():
    '''Главная функция'''

    number_count_default()
    NUMBER_WORDS = value_number_settings()
    data_set = config(NUMBER_WORDS)
    # Если база для накапления не пуста то удалеяем слово из временного списка
    if data_set[0] != False:
        del_word(data_set)
        return run_play(data_set)
    else:
        return run_play(data_set)


