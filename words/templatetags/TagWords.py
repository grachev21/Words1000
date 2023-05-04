from django import template
from words.models import WordsCard
from words.models import Word_Accumulator
from words.models import Word_status

menu = [
        {'title': 'Главная',
        'url_name': 'home'},

        {'title': 'Учить новые слова',
        'url_name': 'learn_new_words'},

        {'title': 'Повторить выученные сегодня',
        'url_name': 'revise_learned_today'},

        {'title': 'Повторить последние 50',
        'url_name': 'repeat_last_50'},

        {'title': 'Выход',
        'url_name': 'out'}
        ]

register = template.Library()

@register.inclusion_tag('words/tag_templates/tag_menu.html')
def menu_header(select):
    return {'menu': menu, 'select': select}
