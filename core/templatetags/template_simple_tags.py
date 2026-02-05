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
            "icon": "cog-6-tooth",
            "icon_class": "w-12 h-12 text-col_bright_1",
        },
        {
            "serve": serve[1],
            "icon": "scale",
            "icon_class": "w-12 h-12 text-col_bright_2",
        },
        {
            "serve": serve[2],
            "icon": "presentation-chart-bar",
            "icon_class": "w-12 h-12 text-col_bright_3",
        },
        {
            "serve": serve[3],
            "icon": "circle-stack",
            "icon_class": "w-12 h-12 text-col_bright_4",
        },
        {
            "serve": serve[4],
            "icon": "book-open",
            "icon_class": "w-12 h-12 text-col_bright_5",
        },
    ]
    return data
