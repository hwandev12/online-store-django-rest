from django import template

register = template.Library()

@register.filter(name="lower")
def lower(value):
    return value.lower()

# create a filter to uppercase letters
@register.filter(name="upper")
def upper(value):
    return value.upper()
