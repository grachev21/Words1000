# core/context_processors.py

def site_settings(request):
    # Эти переменные будут доступны во ВСЕХ шаблонах
    return {
        # 'MENU': [
        #     {"title": "Дом", "url_name": "home"},
        #     {"title": "Список слов", "url_name": "introduction_words"},
        #     {"title": "Учить слова", "url_name": "learn_new_words"},
        #     {"title": "Настройки", "url_name": "settings"},
        # ],
        # 'CURRENT_YEAR': 2024,
        # 'USER_IP': request.META.get('REMOTE_ADDR', ''),
    }
