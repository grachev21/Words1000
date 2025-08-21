from django import template

register = template.Library()


@register.inclusion_tag("header/header.html", takes_context=True)
def header(context):
    menu = [
        {"name": "Главная", "url_name": "home", "img_name": "icons/home.png"},
        {"name": "Слова", "url_name": "words", "img_name": "icons/list.png"},
        {"name": "Учить", "url_name": "game", "img_name": "icons/learn.png"},
        {"name": "Настройки", "url_name": "settings", "img_name": "icons/settings.png"},
    ]

    user_menu = [
        {"name": "Выйти", "url_name": "logout"},
        {"name": "Регистрация", "url_name": "register"},
        {"name": "Войти", "url_name": "login"},
    ]

    return {"menu": menu, "user_menu": user_menu, "request": context["request"]}
