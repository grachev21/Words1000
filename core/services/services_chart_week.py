from users.models import WordsUser
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.db.models import Count


class WeekMixin:
    def dispatch(self, request, *args, **kwargs):
        # Вызываем родительский dispatch сначала
        response = super().dispatch(request, *args, **kwargs)

        # Теперь request доступен, можем получить пользователя
        self.current_user = request.user

        # Сохраняем данные в атрибуты класса
        self.week_data = self.creating_graph(30)
        # self.month_data = self.creating_graph(30)
        # self.season_data = self.creating_graph(90, "days")  # 3 месяца в днях
        # self.half_year_data = self.creating_graph(
        #     180, "days"
        # )  # 6 месяцев в днях
        # self.year_data = self.creating_graph(365, "days")  # 12 месяцев в днях

        return response

    def creating_graph(self, quantity):

        if not self.current_user.is_authenticated:
            return []


        today = timezone.now().date()
        dates = [today - timedelta(days=d) for d in range(quantity)]

        for d in dates:

            obj = WordsUser.objects.filter(
                user=self.current_user,
                status=1,
                created_at__date=str(d)
            )
            print(obj.count(), "|", d)

        # Группируем записи по дате
        # daily_report = (
        #     WordsUser.objects.filter(
        #         user=self.current_user,
        #         status=1,
        #         created_at__date__range=[start_date, today],
        #     )
        #     .extra({"date": "DATE(created_at)"})
        #     .values("date")
        #     .annotate(count=Count("id"))
        #     .order_by("date")
        # )

        # # Создаем полный список дат (включая дни без записей)
        # dates = [today - timedelta(days=i) for i in range(quantity - 1, -1, -1)]

        # # Создаем словарь для быстрого поиска
        # data_dict = {item["date"]: item["count"] for item in daily_report}

        # # Формируем полный отчет
        # complete_report = []
        # for date in dates:
        #     complete_report.append(
        #         {
        #             "date": date,
        #             "count": data_dict.get(date, 0),
        #             "display_date": date.strftime("%d.%m"),
        #             "day_name": date.strftime("%a"),
        #         }
        #     )

        # for day in complete_report:
        #     print(f"Дата: {day['date']}, Записей: {day['count']}")

        # return complete_report

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # Добавляем данные в контекст
    #     context.update(
    #         {
    #             "week_data": getattr(self, "week_data", []),
    #             "month_data": getattr(self, "month_data", []),
    #             "season_data": getattr(self, "season_data", []),
    #             "half_year_data": getattr(self, "half_year_data", []),
    #             "year_data": getattr(self, "year_data", []),
    #             "current_user": self.current_user,
    #         }
    #     )

    #     return context
