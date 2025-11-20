from users.models import WordsUser
from datetime import timedelta
from django.utils import timezone


class ChartMixin:
    def dispatch(self, request, *args, **kwargs):
        # Сначала получаем пользователя
        self.current_user = request.user
        
        # Сразу создаем данные
        self.week_data = self.creating_graph(7)
        # self.month_data = self.creating_graph(30)
        # self.season_data = self.creating_graph(90)
        # self.half_year_data = self.creating_graph(180)
        # self.year_data = self.creating_graph(365)
        
        # Теперь вызываем родительский dispatch
        response = super().dispatch(request, *args, **kwargs)
        return response

    def creating_graph(self, quantity):
        """Создает данные для графика за указанное количество дней."""
        full_date = []

        if not self.current_user.is_authenticated:
            return full_date

        today = timezone.now().date()
        dates = [today - timedelta(days=d) for d in range(quantity)]

        for d in dates:
            obj = WordsUser.objects.filter(
                user=self.current_user, 
                status=1, 
                created_at__date=d  # Убрал str(), используем объект date напрямую
            )
            full_date.append({
                "date_graph": d, 
                "count_graph": obj.count(),
            })

        for f in full_date:
            print(f)

        return full_date

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Безопасно добавляем данные (на случай если dispatch не выполнился)
        context["chart_date"] = {
            "week_data": getattr(self, 'week_data', []),
            # "month_data": getattr(self, 'month_data', []),
            # "season_data": getattr(self, 'season_data', []),
            # "half_year_data": getattr(self, 'half_year_data', []),
            # "year_data": getattr(self, 'year_data', []),
        }

        return context