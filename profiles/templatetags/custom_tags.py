from django import template

register = template.Library()


@register.filter
def friendly_name(string):
    return string.replace('_', ' ')
