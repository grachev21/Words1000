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
    calendarList = []
    calendarFinish = {}

    for calendar in Word_Accumulator.objects.select_related('user').filter(user=user):
        calStr = str(calendar.date.date())
        count.add(calStr)
        calendarList.append(calStr)

    for cou in count:
        num = 0
        for cal in calendarList:
            if cal == cou:
                num += 1
        calendarFinish[cou] = num

    sorted_calendar = dict(sorted(calendarFinish.items()))
    print(sorted_calendar)


    list_label_value = {llv: 'x' for llv in range(0, 7)}
    print(list_label_value)

    for l in range(len(list_label_value)):
        list_label_value['x'] = 33

    print(list_label_value)

    data = {
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

