from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def attr(value, arg):
    bits = arg.split(':')
    if len(bits) != 2:
        raise template.TemplateSyntaxError("Invalid argument for 'attr' filter")
    attr_name, attr_value = bits
    return format_html('{}="{}"', attr_name, attr_value)