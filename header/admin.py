from django.contrib import admin
from .models import Themes


class ThemesAdmin(admin.ModelAdmin):
    list_display = ["theme"]


admin.site.register(Themes, ThemesAdmin)
