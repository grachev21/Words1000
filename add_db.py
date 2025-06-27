import json
from core.models import WordsCard


def record():


    with open('.parser/sw_templates.json', 'r', encoding="utf-8") as file:
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

