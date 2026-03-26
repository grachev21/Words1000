from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"AllWords", views.AllWordsSet)
router.register(r"CardInfoSettings", views.CardInfoiSettingsSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
