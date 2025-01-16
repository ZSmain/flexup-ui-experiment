from django.conf import settings

class DebugWidgetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(response, 'render') and settings.DEBUG:
            if not hasattr(request, '_debug_widget_data'):
                request._debug_widget_data = {}
            response.context_data = getattr(response, 'context_data', {})
            response.context_data['_debug_widget_enabled'] = True
            response.context_data['_debug_widget_data'] = request._debug_widget_data
        return response