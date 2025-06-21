from django import template
from header.models import Menu, LoginLogout, Logo

register = template.Library()


@register.inclusion_tag("includes/header.html", takes_context=True)
def header(context):

    data_header = {
        "menu": Menu.objects.all(),
        "login_logout": LoginLogout.objects.all(),
        "logo": Logo.objects.last(),
        "request": context["request"],
    }
    return data_header
