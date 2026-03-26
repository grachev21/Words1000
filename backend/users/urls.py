from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"RemainderCardInfo", views.RemainderCardInfoSet, basename="remaindercardinfo")
router.register(r"ChartWeek", views.ChartWeekSet, basename="chartweek")
router.register(r"ChartMonth", views.ChartMonthSet, basename="chartmonth")
router.register(r"ChartYear", views.ChartYearSet, basename="chartyear")

urlpatterns = [
    path("api/", include(router.urls)),
]
