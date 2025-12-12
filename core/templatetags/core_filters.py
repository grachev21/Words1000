import ast

from django import template

register = template.Library()


@register.filter
def list_variable(btn):
    return [b.split("-") for b in btn.split(",")]

@register.simple_tag
def create_list(*args):
    return list(args)



@register.simple_tag
def zip_list(*args):
    return zip(*args)