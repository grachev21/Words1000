from datetime import timedelta, date
from tracemalloc import start
import calendar

from django.utils import timezone

from users.models import WordsUser

WEEKDAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]


class ChartMixin:
    def dispatch(self, request, *args, **kwargs):
        # Сначала получаем пользователя
        self.current_user = request.user

        # Сразу создаем данные
        self.week_data = self.create_graph_week()
        self.month_data = self.creating_graph(quantity=30, breakdown=7)
        # self.season_data = self.creating_graph(quantity=91, breakdown=30)
        # self.half_year_data = self.creating_graph(quantity=180, breakdown=7)
        # self.year_data = self.creating_graph(quantity=365)

        # self.filter_date()
        # Теперь вызываем родительский dispatch
        # self.create_graph_week()
        response = super().dispatch(request, *args, **kwargs)
        return response

    def create_graph_week(self):
        full_date = []
        if not self.current_user.is_authenticated:
            return full_date

        today = timezone.now().date()

        # ***
        def day_var():
            today = date.today()
            full_list = [
                today,
            ]
            first_day = today.replace(day=1)
            last_day = first_day.replace(
                day=calendar.monthrange(today.year, today.month)[1]
            )

            while today != first_day:
                if today.weekday() == 0:
                    if not today in full_list:
                        full_list.append([today, [today - timedelta(days=d) for d in range(7)]])  
                today -= timedelta(days=1)
            print(full_list)

        day_var()

        dates = sorted([today - timedelta(days=d) for d in range(7)])

        for d in dates:
            obj = WordsUser.objects.filter(
                user=self.current_user,
                status=1,
                created_at__date=d,  # Убрал str(), используем объект date напрямую
            )
            full_date.append(
                {
                    "date_graph": f"{WEEKDAYS[d.weekday()]} - {d.day}",
                    "count_graph": obj.count(),
                }
            )
        return full_date

    def creating_graph(self, quantity=7, breakdown=7):
        full_date = []

        if not self.current_user.is_authenticated:
            return full_date

        today = timezone.now()
        dates = sorted(
            [today - timedelta(days=d) for d in range(0, quantity, breakdown)]
        )
        dates_out = list(zip(dates, dates[1:]))

        for i in dates_out:
            obj = WordsUser.objects.filter(
                user=self.current_user,
                status=1,
                created_at__range=[i[0], i[1]],
            ).count()

            full_date.append(
                {
                    "date_graph": i[1].date(),
                    "count_graph": obj,
                }
            )

        return full_date

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Безопасно добавляем данные (на случай если dispatch не выполнился)
        context["chart_date"] = {
            "week_data": getattr(self, "week_data", []),
            "month_data": getattr(self, "month_data", []),
            # "season_data": getattr(self, "season_data", []),
            # "half_year_data": getattr(self, "half_year_data", []),
            # "year_data": getattr(self, "year_data", []),
        }

        return context
