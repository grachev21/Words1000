import calendar
from datetime import date, datetime, timedelta

from django.utils import timezone

from users.models import WordsUser

WEEKDAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]


class ChartMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.current_user = request.user
            self.week_data = self.create_graph_week()
            self.month_data = self.creating_graph_month(quantity=30, breakdown=7)
            self.year_data = self.creating_graph_year()

        response = super().dispatch(request, *args, **kwargs)
        return response

    def create_graph_week(self):
        full_date = []
        today = timezone.now().date()
        dates = sorted([today - timedelta(days=d) for d in range(7)])

        for d in dates:
            full_date.append(
                {
                    "date_graph": f"{WEEKDAYS[d.weekday()]} - {d.day}",
                    "count_graph": self.request_db(d),
                }
            )
        return full_date

    def creating_graph_month(self, quantity=7, breakdown=7):
        full_date = []

        today = date.today()
        first_day = today.replace(day=1)
        last_day = first_day.replace(
            day=calendar.monthrange(today.year, today.month)[1]
        )

        current_day = last_day
        while current_day.day > 1:
            current_day -= timedelta(days=1)
            full_date.append(
                {
                    "date_graph": current_day if current_day.weekday() == 0 else "",
                    "count_graph": self.request_db(current_day),
                }
            )
        return full_date

    def creating_graph_year(self):
        full_date = []

        for d in range(1, 13):
            first_day = datetime(datetime.now().year, d, 1)
            last_day = first_day.replace(
                day=calendar.monthrange(first_day.year, first_day.month)[1]
            )

            full_date.append(
                {
                    "date_graph": calendar.month_name[first_day.month],
                    "count_graph": self.request_db(
                        [first_day, last_day], range_day=True
                    ),
                }
            )

        return full_date

    def request_db(self, value, range_day=False):
        query = WordsUser.objects.filter(user=self.current_user, status=4)
        if range_day:
            query = query.filter(created_at__range=value)
        else:
            query = query.filter(created_at__date=value)
        return query.count()

    def get_data_chart(self):

        data = {
            "week_data": getattr(self, "week_data", []),
            "month_data": getattr(self, "month_data", []),
            "year_data": getattr(self, "year_data", []),
        }
        print(data, "<<<")
        return data
