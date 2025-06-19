from django.contrib import admin
from header.models import Menu


@admin.register(Menu)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
