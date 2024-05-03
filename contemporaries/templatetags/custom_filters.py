from django import template

register = template.Library()


@register.filter(name='css_class')
def css_class(value):
    return 'occupation-' + value.replace(' ', '-').replace('_', '-').lower()
