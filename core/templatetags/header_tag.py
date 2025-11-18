# Header tag

from django import template

register = template.Library()


@register.inclusion_tag("header/header.html", takes_context=True)
def header(context, active_page):
    print(context["active_page"])
    menu = [
        {
            "name": "Главная",
            "url_name": {"app": "core", "url": "home"},
            "img_name": "icons/home.png",
        },
        {
            "name": "Слова",
            "url_name": {"app": "core", "url": "words"},
            "img_name": "icons/list.png",
        },
        {
            "name": "Учить",
            "url_name": {"app": "game", "url": "game"},
            "img_name": "icons/learn.png",
        },
        {
            "name": "Настройки",
            "url_name": {"app": "settings", "url": "settings"},
            "img_name": "icons/settings.png",
        },
    ]

    user_menu = [
        {"name": "Выйти", "url_name": "logout"},
        {"name": "Регистрация", "url_name": "register"},
        {"name": "Войти", "url_name": "login"},
    ]

    return {"menu": menu, "user_menu": user_menu, "request": context["request"], "active_page": active_page}
