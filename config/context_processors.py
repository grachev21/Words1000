from django.conf import settings
from django.utils import timezone


def global_context(request):
    """Глобальный контекст для всех шаблонов"""
    return {
        "menu": [
            {
                "name": "Главная",
                "url_name": "home",
                "img_name": "icons/home.png",
            },
            {
                "name": "Слова",
                "url_name": "words",
                "img_name": "icons/list.png",
            },
            {
                "name": "Учить",
                "url_name": "game",
                "img_name": "icons/learn.png",
            },
            {
                "name": "Настройки",
                "url_name": "settings",
                "img_name": "icons/settings.png",
            },
        ],
        "user_menu": [
            {"name": "Выйти", "url_name": "logout"},
            {"name": "Регистрация", "url_name": "register"},
            {"name": "Войти", "url_name": "login"},
        ],
    }
