from .menu import SIDEBAR_MENU, BOTTOM_MENU

def menu_context(request):
    return {
        'sidebar_menu': SIDEBAR_MENU,
        'bottom_menu': BOTTOM_MENU,
        'is_dashboard': request.path.startswith('/dashboard')
    }
