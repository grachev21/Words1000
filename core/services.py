from settings.models import WordsSettings
from users.models import WordsUser
from core.models import WordsCard
from datetime import date


class ServicesMixin:
    """
    Sends data to the context for the
    service panel on the main panel of the user.

    Args:
        user, context.
    """

    @staticmethod
    def data_incision(user):

        if WordsSettings.objects.filter(user=user).exists():
            settings_words = WordsSettings.objects.filter(user=user).latest("id")

        today_words = WordsUser.objects.filter(
            user=user, status="4", created_at=date.today()
        ).count()

        remainder_words = WordsUser.objects.filter(
            user=user, status="2"
        ).count()

        all_words = WordsUser.objects.filter(user=user, status="1").count()
        all_words_studied = WordsUser.objects.filter(
            user=user, status="4"
        ).count()

        return [
            {
                "name": "Настройки",
                "description": "Количество слов которое стоит в настройках",
                "data": settings_words.number_words if user.is_authenticated else 23,
            },
            {
                "name": "Количество слов за день",
                "description": "Общее количество слов выученные за текущий день",
                "data": (today_words if user.is_authenticated else 23),
            },
            {
                "name": "Осталось за день",
                "description": "Эти слова вы должны выучить сегодня",
                "data": (remainder_words if user.is_authenticated else 3),
            },
            {
                "name": "Всего",
                "description": "Это все слова которые присутствуют в словаре",
                "data": all_words if user.is_authenticated else 32,
            },
            {
                "name": "Выучено",
                "description": "Это общее количество слов которое вы выучили за все время",
                "data": all_words_studied if user.is_authenticated else 11,
            },
        ]

    def init_data(self, user, check_user, context):
        if not user or not context or check_user:
            return context

        services_data = self.data_incision(user)

        context.update(
            {
                "services_data": services_data,
                "all_words": WordsCard.objects.all(),
            }
        )

        return context


class WordsMixin:

    @staticmethod
    def info_bar(user):
        obj = WordsUser.objects.filter(user=user)
        return [
            {"data": obj.count(), "title": "Все"},
            {"data": obj.filter(status="1").count(), "title": "Неизвестно"},
            {"data": obj.filter(status="2").count(), "title": "Изучаю"},
            {"data": obj.filter(status="3").count(), "title": "Повторяю"},
            {"data": obj.filter(status="4").count(), "title": "Изучил"},
        ]

    def init_data(self, user, context):
        context.update({"info_bar_data": self.info_bar(user)})

        return context

    @staticmethod
    def filter(status, user):
        # Получаем параметр фильтра из GET-запроса
        status_filter = status 

        # Фильтруем слова для текущего пользователя
        words_user = WordsUser.objects.filter(user=user)

        if status_filter:
            words_user = words_user.filter(status=status_filter)

        return {"status_filter": status_filter, "words_user": words_user}
