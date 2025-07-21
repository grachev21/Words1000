from users.models import WordsUser


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
