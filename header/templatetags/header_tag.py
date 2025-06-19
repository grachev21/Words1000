from django import template
from header.models import Menu, LoginLogout, Logo

register = template.Library()


@register.inclusion_tag("templatetags/header.html")
def header():
    data = {"menu": Menu.objects.all(),
            "login_logout":  LoginLogout.objects.all(),
            "logo":  Logo.objects.all()}

    return data
