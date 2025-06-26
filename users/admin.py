from django.contrib import admin
from models import WordsUser, WordsSettings


@admin.register(WordsUser)
class WordsUserAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "number_repetitions",
        "status",
        "show",
        "user",
        "core_words",
    )  # Поля для отображения в списке
    # list_filter = ("field1", "field2")  # Фильтры справа
    # search_fields = ("field1", "field2")  # Поля для поиска
    # ordering = ("-created_at",)  # Сортировка

@admin.register(WordsSettings)
class WordsSettingsAdmin(WordsSettings):
    list_display = ("number_words", "number_repetitions", "user")

