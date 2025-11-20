from django.urls import path

from . import views


urlpatterns = [
    path("settings/", views.SettingsPage.as_view(), name="settings"),
    path(
        "resettings_dictionaries/",
        views.ResettingDictionaries.as_view(),
        name="resettings_dictionaries",
    ),
]
