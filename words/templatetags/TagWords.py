import datetime as dc
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

    def create_dict_result():
        count = set()
        calendarList = []
        calendarFinish = []

        for calendar in Word_Accumulator.objects.select_related('user').filter(user=user):
            calStr = str(calendar.date.date())
            count.add(calStr)
            calendarList.append(calStr)

        for cou in count:
            num = 0
            for cal in calendarList:
                if cal == cou:
                    num += 1
            calendarFinish.append((cou, num))
        return calendarFinish

    def connect_date_value(value):
        dateList = [(str(dc.datetime.today() - dc.timedelta(days=x))[0:10], '') for x in range(7)]

        for index in reversed(range(len(dateList))):
            for val in value:
                if dateList[index][0] == val[0]:
                    dateList[index] = val
        x = dateList.reverse()
        print(x)
        return dateList

    dateList = connect_date_value(create_dict_result())

    data = {
        'dateList': dateList
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

