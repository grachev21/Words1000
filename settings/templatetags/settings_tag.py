from django import template
from settings.models import WordsSettings


register = template.Library()
#
#
# @register.inclusion_tag("includes/home/services.html", takes_context=True)
# def services(context, index):
#
#     settings_words = None
#     settings_word_day = None
#     # Data for services
#     request = context["request"]
#     user = request.user
#     if user.is_authenticated:
#         if WordsSettings.objects.filter(user=user).exists():
#             settings_words = WordsSettings.objects.filter(
#                 user=user).latest("id")
#             settings_word_day = WordsSettings.objects.filter(user=user).all()
#
#     # Strict data
#     data_services = [
#         {
#             "name": "Настройки",
#             "description": "Количество слов которое стоит в настройках",
#             "data": settings_words.number_words if settings_words else 23,
#         },
#         {
#             "name": "Количество слов за день",
#             "description": "Общее количество слов выученные за текущий день",
#             "data": settings_word_day if settings_word_day else 23,
#         },
#         {
#             "name": "Осталось за день",
#             "description": "Эти слова вы должны выучить сегодня",
#             "data": settings_word_day if settings_word_day else 3,
#         },
#         {
#             "name": "Всего",
#             "description": "Это все слова которые присутствуют в словаре",
#             "data": settings_word_day if settings_word_day else 32,
#         },
#         {
#             "name": "Выучено",
#             "description": "Это общее количество слов которое вы выучили за все время",
#             "data": settings_word_day if settings_word_day else 11,
#         },
#     ]
#
#     return {
#         "data_services": data_services,
#         "index": index,
#     }
