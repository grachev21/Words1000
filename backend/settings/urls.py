from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"SettingsWords", views.SettingsWordsSet, basename="settingswords")

app_name = "settings"
urlpatterns = [
    path("", include(router.urls))
]
