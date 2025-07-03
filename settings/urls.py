from django.urls import path
from settings.views import SettingsPage, ResettingDictionaries
from django.urls import path


urlpatterns = [
    path("settings/", SettingsPage.as_view(), name="settings"),
    path("resettings_dictionaries/", ResettingDictionaries.as_view(), name="resettings_dictionaries"),
]
