from django.contrib import admin
from settings.models import WordsSettings


@admin.register(WordsSettings)
class WordsSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "number_words",
        "number_repetitions",
        "user"
    )  
