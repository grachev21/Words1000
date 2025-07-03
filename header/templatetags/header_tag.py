from django import template

register = template.Library()


@register.inclusion_tag("includes/header.html", takes_context=True)
def header(context):
    menu = [
        {"name": "Главная", "url_name": "home"},
        {"name": "Ознакомится со списком", "url_name": "words"},
        {"name": "Учить новые слова", "url_name": "game"},
        {"name": "Настройки", "url_name": "settings"},
    ]

    user_menu = [
        {"name": "Выйти", "url_name": "logout"},
        {"name": "Регистрация", "url_name": "register"},
        {"name": "Войти", "url_name": "login"},
    ]

    return {"menu": menu, "user_menu": user_menu, "request": context["request"]}
