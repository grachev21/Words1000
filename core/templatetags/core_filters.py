import ast

from django import template

register = template.Library()


@register.filter
def list_variable(btn):
    return [b.split("-") for b in btn.split(",")]
