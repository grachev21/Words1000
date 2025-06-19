from django.db import models


class Logo(models.Model):
    image = models.ImageField(
        upload_to="photos/", null=True, verbose_name="Логотип")

    class Meta:
        verbose_name = "logo"
        verbose_name_plural = "logo"


class Menu(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="name")
    link = models.CharField(max_length=200, null=True,
                            unique=True, verbose_name="link")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


class LoginLogout(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="name")
    link = models.CharField(max_length=200, null=True,
                            unique=True, verbose_name="link")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "LoginLogout"
        verbose_name_plural = "LoginLogout"
