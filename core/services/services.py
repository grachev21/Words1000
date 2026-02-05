from datetime import date
import random

from core.models import WordsCard
from settings.models import WordsSettings
from users.models import WordsUser


class ServicesMixin:
    """
    Mixin for page Home.
    Sends data to the context for the
    service panel on the main panel of the user.

    Args:
        user, context.
    """

    @staticmethod
    def data_incision(user):
        """
        Return list of data for the service panel

        Args:
            user: The user object.
        """
        if WordsSettings.objects.filter(user=user).exists():
            settings_words = WordsSettings.objects.filter(user=user).latest("id")

        today_words = WordsUser.objects.filter(
            user=user, status="4", created_at=date.today()
        ).count()

        remainder_words = WordsUser.objects.filter(user=user, status="2").count()

        all_words = WordsUser.objects.filter(user=user, status="1").count()
        all_words_studied = WordsUser.objects.filter(user=user, status="4").count()

        return [
            {
                "name": "Настройки",
                "description": "Количество слов которое стоит в настройках",
                "data": (settings_words.number_words if user.is_authenticated else 23),
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
                "serve": services_data,
                "all_words": WordsUser.objects.filter(user=user),
            }
        )

        return context


class WordsMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.request = request

            self.info_bar = self.create_info_bar()
            self.filter = self.create_filter()
            self.status = WordsUser.Status.choices

        response = super().dispatch(request, *args, **kwargs)
        return response

    def create_info_bar(self):
        obj = WordsUser.objects.filter(user=self.request.user)
        return [
            {"data": obj.count(), "title": "Все"},
            {"data": obj.filter(status="1").count(), "title": "Неизвестно"},
            {"data": obj.filter(status="2").count(), "title": "Изучаю"},
            {"data": obj.filter(status="3").count(), "title": "Повторяю"},
            {"data": obj.filter(status="4").count(), "title": "Изучил"},
        ]

    def create_filter(self):
        words_user = WordsUser.objects.filter(user=self.request.user)
        status = self.request.GET.get("status")

        if status:
            words_user = words_user.filter(status=status)

        return {"status_filter": status, "words_user": words_user}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "info_bar_data": self.info_bar,
                "words_user": self.filter["words_user"],
                "status_choices": self.status,
                "current_status": int(self.filter["status_filter"])if self.filter["status_filter"] else None,
                "btn_status": (
                    [
                        status
                        for status in self.status
                        if status[0] == int(self.filter["status_filter"])
                    ][0][1]
                    if self.filter["status_filter"]
                    else "Все статусы"
                ),
            }
        )
        return context
