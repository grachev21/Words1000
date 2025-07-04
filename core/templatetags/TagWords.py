import datetime as dc
from datetime import datetime
from django import template
from users.models import WordsUser
from settings.models import WordsSettings

register = template.Library()


@register.inclusion_tag("includes/tag_footer.html")
def footer():
    current_datetime = datetime.now()
    return {"current_date": current_datetime.year}


@register.inclusion_tag("includes/home/chart_week.html")
def chart_week(user):

    def create_dict_result():
        count = set()
        calendarList = []
        calendarFinish = []

        for calendar in WordsUser.objects.select_related("user").filter(user=user):
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
        dateList = [
            (str(dc.datetime.today() - dc.timedelta(days=x))[0:10], "")
            for x in range(14)
        ]

        for index in reversed(range(len(dateList))):
            for val in value:
                if dateList[index][0] == val[0]:
                    dateList[index] = val
        x = dateList.reverse()
        print(x)
        return dateList

    dateList = connect_date_value(create_dict_result())

    data = {"dateList": dateList}

    return data


@register.inclusion_tag("includes/home/doughnut.html")
def doughnut(*args):
    data = {"value": list(args)}
    return data




@register.inclusion_tag("includes/progress_bar_revise_learned.html")
def progress_bar_revise_learned():
    data = {}

    return data
