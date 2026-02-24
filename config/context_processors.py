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
            {"name": "Выйти", "link": "account_logout"},
            {"name": "Регистрация", "link": "account_signup"},
            {"name": "Войти", "link": "account_login"},
        ],
    }
