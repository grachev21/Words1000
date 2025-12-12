import datetime as dc
from datetime import datetime
from django import template
from users.models import WordsUser


register = template.Library()


@register.simple_tag
def card_data(serve):

    data = [
        {
            "serve": serve[0],
            "icon": "settings",
            "icon_class": "w-12 h-12 text-col_bright_1",
        },
        {
            "serve": serve[1],
            "icon": "weight",
            "icon_class": "w-12 h-12 text-col_bright_2",
        },
        {
            "serve": serve[2],
            "icon": "weight",
            "icon_class": "w-12 h-12 text-col_bright_3",
        },
        {
            "serve": serve[3],
            "icon": "balance",
            "icon_class": "w-12 h-12 text-col_bright_4",
        },
        {
            "serve": serve[4],
            "icon": "learn",
            "icon_class": "w-12 h-12 text-col_bright_5",
        },
    ]
    return data
