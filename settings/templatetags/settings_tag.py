from django import template
from core.models import WordsCard
from settings.models import WordsSettings
from users.models import WordsUser

register = template.Library()


@register.inclusion_tag("includes/home/services.html", takes_context=True)
def services(context, index):

    settings_word_day = None
    # Data for services
    request = context["request"]
    user = request.user
    if user.is_authenticated:
        if WordsSettings.objects.filter(user=user).exists():
            settings_words = WordsSettings.objects.filter(user=user).latest("id")
            settings_word_day = WordsSettings.objects.filter(user=user).all()

    

    # Strict data
    data = [
        {
            "name": "Настройки",
            "description": "Количество слов которое стоит в настройках",
            "data": settings_words.number_words if settings_words else 23,
        },
        {
            "name": "Количество слов за день",
            "description": "Общее количество слов выученные за текущий день",
            "data": settings_word_day if settings_word_day else 23,
        },
        {
            "name": "Осталось за день",
            "description": "Эти слова вы должны выучить сегодня",
            "data": settings_word_day if settings_word_day else 23,
        },
        {
            "name": "Всего",
            "description": "Это все слова которые присутствуют в словаре",
            "data": settings_word_day if settings_word_day else 23,
        },
        {
            "name": "Выучено",
            "description": "Это общее количество слов которое вы выучили за все время",
            "data": settings_word_day if settings_word_day else 23,
        },
    ]

    return {
        "data": data[index],
        "index": index,
    }
