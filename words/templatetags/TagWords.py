from datetime import datetime
from django import template
from ..models import SettingsWordNumber
from ..models import WordsToRepeat
from ..models import Word_Accumulator

register = template.Library()

@register.inclusion_tag('words/tag_templates/tag_footer.html')
def footer():
    current_datetime = datetime.now()
    return {'current_date': current_datetime.year}

@register.inclusion_tag('words/tag_templates/chart_week.html')
def chart_week(user):
    count = set()
    calendar = {}
    list_calendar = [calendar.date.day for calendar in Word_Accumulator.objects.select_related('user').filter(user=user)]

    print(list_calendar, calendar, '<<<')
    data = {
        'week': 0
    }
    return data

@register.inclusion_tag('words/tag_templates/doughnut.html')
def doughnut(*args):
    data = {
            'value': list(args)
        }
    return data

@register.inclusion_tag('words/tag_templates/progress_bar_learn_new_words.html')
def progress_bar_learn_new_words(**kwargs):
    settin_words = SettingsWordNumber.objects.select_related('user').get(user=kwargs['user']).number_words
    count_words = settin_words - WordsToRepeat.objects.select_related('user').filter(user=kwargs['user']).count()
    out = settin_words / 100
    result = count_words / out
    data = {
        'count_words': int(result)
    }
    return data
    

@register.inclusion_tag('words/tag_templates/progress_bar_revise_learned.html')
def progress_bar_revise_learned():
    data = {

    }

    return data

