from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"AllWords", views.AllWordsSet, basename="allwords")
router.register(r"CardInfoSettings", views.CardInfoiSettingsSet)

urlpatterns = [
    path("", include(router.urls)),
]
