import csv
from words.models import WordsCard

words_en = []
transcription = []
words_ru = []
phrases_en = []
phrases_ru = []

with open('.parser/db_1000_words.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        words_en.append(r[0].strip())
        transcription.append(r[1].strip())
        words_ru.append(r[2].strip())
        phrases_en.append(r[3].strip())
        phrases_ru.append(r[4].strip())

def record():
    for value in range(0, 1001):
        mod = WordsCard(word_en=words_en[value],
                        transcription=transcription[value],
                        word_ru=words_ru[value],
                        phraze_en=phrases_en[value],
                        phraze_ru=phrases_ru[value])
        mod.save()
