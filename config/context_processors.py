def global_context(request):
    return {
        "menu": [
            {
                "name": "Главная",
                "url_name": "home",
                "img_name": "home",
            },
            {
                "name": "Слова",
                "url_name": "words",
                "img_name": "list",
            },
            {
                "name": "Учить",
                "url_name": "game",
                "img_name": "learn",
            },
            {
                "name": "Настройки",
                "url_name": "settings",
                "img_name": "settings",
            },
        ],
        "user_menu": [
            {"name": "Выйти", "url_name": "logout"},
            {"name": "Регистрация", "url_name": "register"},
            {"name": "Войти", "url_name": "login"},
        ],
    }
