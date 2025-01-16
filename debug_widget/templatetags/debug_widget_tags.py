from django import template
from django.conf import settings

register = template.Library()

@register.filter
def is_dict(value):
    return isinstance(value, dict)

@register.filter
def is_list(value):
    return isinstance(value, (list, tuple))

@register.inclusion_tag('debug_widget/widget.html', takes_context=True)
def render_debug_widget(context):
    return {
        'debug_data': context.get(getattr(settings, 'DEBUG_WIDGET_CONTEXT_VAR', 'DEBUG_DATA'), {}),
        'widget_position': getattr(settings, 'DEBUG_WIDGET_POSITION', 'right'),
        'widget_theme': getattr(settings, 'DEBUG_WIDGET_THEME', 'light'),
    }