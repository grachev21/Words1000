from datetime import date
import random

from core.models import WordsCard
from settings.models import WordsSettings
from users.models import WordsUser




class WordsMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.request = request

            self.info_bar = self.create_info_bar()
            self.filter = self.create_filter()
            self.status = WordsUser.Status.choices

        return super().dispatch(request, *args, **kwargs)

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
