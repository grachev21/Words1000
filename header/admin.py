from django.contrib import admin
from header.models import Menu, LoginLogout, Logo


@admin.register(Menu)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("name", "link")

@admin.register(LoginLogout)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("name", "link")

@admin.register(Logo)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("image",)