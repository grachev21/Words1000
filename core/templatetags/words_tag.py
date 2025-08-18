import datetime as dc
from datetime import datetime
from django import template
from users.models import WordsUser


register = template.Library()


@register.inclusion_tag("includes/tag_footer.html")
def footer():
    current_datetime = datetime.now()
    return {"current_date": current_datetime.year}


@register.inclusion_tag("includes/home/doughnut.html")
def doughnut(*args):
    data = {"value": list(args)}
    return data


@register.inclusion_tag("includes/progress_bar_revise_learned.html")
def progress_bar_revise_learned():
    data = {}

    return data
