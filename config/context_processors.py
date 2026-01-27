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
                "img_name": "list-bullet",
            },
            {
                "name": "Учить",
                "url_name": "game",
                "img_name": "book-open",
            },
            {
                "name": "Настройки",
                "url_name": "settings",
                "img_name": "cog-6-tooth",
            },
        ],
        "user_menu": [
            {"name": "Выйти", "url_name": "logout"},
            {"name": "Регистрация", "url_name": "register"},
            {"name": "Войти", "url_name": "login"},
        ],
    }
