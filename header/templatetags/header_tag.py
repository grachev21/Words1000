from django import template
from header.models import Menu, LoginLogout, Logo

register = template.Library()

@register.inclusion_tag("templatetags/header/header.html")
def header():
    data_header = {
        # "menu": Menu.objects.all(),
        # "login_logout": LoginLogout.objects.all(),
        # "logo": Logo.objects.all(),
        "x":"hello"
    }
    return data_header
