from django.contrib import admin
from .models import WordsCard


class WordsCardAdmin(admin.ModelAdmin):
    list_display = (
        "word_en",
        "transcription",
        "word_ru",
        "phrases_en",
        "phrases_ru",
    )
    search_fields = ("word_en",)
