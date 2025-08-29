from django.contrib import admin
from .models import WordsCard


@admin.register(WordsCard)
class WordsCardAdmin(admin.ModelAdmin):
    list_display = (
        "word_en",
        "word_ru",
        "transcription",
        "phrases_en",
        "phrases_ru",
    )
    search_fields = ("word_en",)
