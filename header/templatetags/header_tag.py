from django import template

register = template.Library()


@register.inclusion_tag("includes/header.html", takes_context=True)
def header(context):
    menu = [
        {"name": "Главная", "url_name": "home", "img_path": "icons/home.png"},
        {"name": "Слова", "url_name": "words", "img_path": "icons/list.png"},
        {"name": "Учить", "url_name": "game", "img_path": "icons/learn.png"},
        {"name": "Настройки", "url_name": "settings", "img_path": "icons/settings.png"},
    ]

    user_menu = [
        {"name": "Выйти", "url_name": "logout"},
        {"name": "Регистрация", "url_name": "register"},
        {"name": "Войти", "url_name": "login"},
    ]

    return {"menu": menu, "user_menu": user_menu, "request": context["request"]}
