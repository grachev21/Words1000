from datetime import timedelta

from django.utils import timezone

from users.models import WordsUser


class ChartMixin:
    def dispatch(self, request, *args, **kwargs):
        # Сначала получаем пользователя
        self.current_user = request.user

        # Сразу создаем данные
        self.week_data = self.create_graph_week()
        self.month_data = self.creating_graph(42)
        # self.season_data = self.creating_graph(90)
        # self.half_year_data = self.creating_graph(180)
        # self.year_data = self.creating_graph(365)

        # self.filter_date()
        # Теперь вызываем родительский dispatch
        self.create_graph_week()
        response = super().dispatch(request, *args, **kwargs)
        return response

    def create_graph_week(self):
        full_date = []
        WEEKDAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
        if not self.current_user.is_authenticated:
            return full_date

        today = timezone.now().date()
        dates = [today - timedelta(days=d) for d in range(7)]

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

    def creating_graph(self, quantity):
        """Создает данные для графика за указанное количество дней."""
        full_date = []

        if not self.current_user.is_authenticated:
            return full_date

        today = timezone.now().date()
        dates = [(today - timedelta(days=d)) for d in range(quantity) if (today - timedelta(days=d)).weekday() == 0]

        for value in list(zip(dates[:-1], dates[1:])):
            print(value[0])
            print(value[1])
            obj = WordsUser.objects.filter(
                user=self.current_user,
                status=1,
                created_at__range=[value[0], value[1]],   # Убрал str(), используем объект date напрямую
            )
            print(obj)
            full_date.append(
                {
                    "date_graph": value[0],
                    "count_graph": obj.count(),
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
