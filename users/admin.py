from django.contrib import admin
from users.models import WordsUser
from django.contrib import admin
from .models import User

admin.site.register(User)


@admin.register(WordsUser)
class WordsUserAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "number_repetitions",
        "status",
        "user",
        "core_words",
    )  # Поля для отображения в списке
    # list_filter = ("field1", "field2")  # Фильтры справа
    # search_fields = ("field1", "field2")  # Поля для поиска
    # ordering = ("-created_at",)  # Сортировка
