from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter()
router.register(
    r"RemainderCardInfo", views.RemainderCardInfoSet, basename="remaindercardinfo"
)
router.register(r"ChartWeek", views.ChartWeekSet, basename="chartweek")
router.register(r"ChartMonth", views.ChartMonthSet, basename="chartmonth")
router.register(r"ChartYear", views.ChartYearSet, basename="chartyear")
router.register(r"ListWord", views.ListWordSet, basename="listword")

urlpatterns = [
    path("", include(router.urls)),
]
