from datetime import timedelta 
from django.utils import timezone
from datetime import date, timedelta, datetime
from users.models import WordsUser
import calendar


WEEKDAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]

def request_db(user, value, range_day=False):
    query = WordsUser.objects.filter(user=user, status="1")  
    if range_day:
        query = query.filter(created_at__range=value)
        return query.count()
    else:
        query = query.filter(created_at__date=value)
        return query.count()

class ChartWeekMixin:
    def get_week_data(self, user):
        full_date = []
        today = timezone.now().date()
        dates = sorted([today - timedelta(days=d) for d in range(7)])

        for d in dates:
            full_date.append(
                {
                    "date_graph": f"{WEEKDAYS[d.weekday()]} - {d.day}",
                    "count_graph": request_db(user, d, range_day=False),
                }
            )
        return full_date

class ChartMonthMixin:
    def get_month_data(self, user, quantity=7, breakdown=7):
        full_date = []

        today = date.today()
        first_day = today.replace(day=1)
        last_day = first_day.replace(day=calendar.monthrange(today.year, today.month)[1])

        current_day = last_day
        while current_day.day > 1:
            current_day -= timedelta(days=1)
            full_date.append(
                {
                    "date_graph": current_day if  current_day.weekday() == 0 else "",
                    "count_graph": request_db(user, current_day),
                }
            )
        return full_date

class ChartYearMixin:
    def get_year_data(self, user):
        full_date = []

        for d in range(1, 13):
            first_day = datetime(datetime.now().year, d, 1)
            last_day = first_day.replace(day=calendar.monthrange(first_day.year, first_day.month)[1])

            full_date.append(
                {
                    "date_graph": calendar.month_name[first_day.month],
                    "count_graph": request_db(user, [first_day, last_day], range_day=True),
                }
            )

        return full_date