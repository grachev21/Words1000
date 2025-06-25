from django.db import models


class Themes(models.Model):
    theme = models.BooleanField(default=True, verbose_name="Тема")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
