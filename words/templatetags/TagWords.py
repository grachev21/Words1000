from datetime import datetime
from django import template
from words.models import WordsCard
from words.models import Word_Accumulator
from words.models import Word_status
from words.models import SettingsWordNumber
from words.models import WordsToRepead

menu = [
        {'title': 'Главная',
        'url_name': 'home'},

        {'title': 'Знакомство со словами',
        'url_name': 'introduction_words'},

        {'title': 'Учить новые слова',
        'url_name': 'learn_new_words'},

        {'title': 'Повторить выученные',
        'url_name': 'revise_learned'},

        {'title': 'Настройки',
        'url_name': 'settings'},

        {'title': 'Выход',
        'url_name': 'out'},
        ]

register = template.Library()

@register.inclusion_tag('words/tag_templates/tag_menu.html')
def menu_header(select):
        return {'menu': menu, 'select': select}


@register.inclusion_tag('words/tag_templates/tag_info.html')
def info_header(line_off_on):
    total_words = WordsCard.objects.count() - Word_Accumulator.objects.count()
    counter_word = WordsToRepead.objects.all().count()
    number = SettingsWordNumber.objects.first()
    total = Word_Accumulator.objects.count()
    return {'number': number, 'counter_word': counter_word, 'total_words': total_words, 'total': total, 'line_off_on':line_off_on}


@register.inclusion_tag('words/tag_templates/tag_footer.html')
def footer():
    current_datetime = datetime.now()
    return {'current_date': current_datetime.year}
