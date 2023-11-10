import json
from words.models import WordsCard
from words.models import RepeatNumber


def record():

    list_repeat = ['one', 'two', 'tree']

    with open('.parser/sw_templates.json', 'r') as file:
        data = json.load(file)

    for value in data:
        mod = WordsCard(
                word_en=value['word_en'],
                word_ru=value['word_ru'],
                transcription=value['transcription'],
                phrases_en=value['exemple_en'],
                phrases_ru=value['exemple_ru']
        )
        mod.save()

    for repeat in list_repeat:
        rep = RepeatNumber(number=repeat)
        rep.save()
