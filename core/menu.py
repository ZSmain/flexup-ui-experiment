SIDEBAR_MENU = [
    {
        'icon': '📊',
        'label': 'Overview',
        'href': '/dashboard',
        'children': []
    },
    {
        'icon': '📈',
        'label': 'Analytics',
        'href': '/dashboard/analytics',
        'children': [
            {'icon': '📑', 'label': 'Reports', 'href': '/dashboard/analytics/reports'},
            {'icon': '📊', 'label': 'Statistics', 'href': '/dashboard/analytics/statistics'},
            {'icon': '📈', 'label': 'Performance', 'href': '/dashboard/analytics/performance'}
        ]
    },
    {
        'icon': '⚙️',
        'label': 'Settings',
        'href': '/dashboard/settings',
        'children': [
            {'icon': '👤', 'label': 'Profile', 'href': '/dashboard/settings/profile'},
            {'icon': '🔒', 'label': 'Security', 'href': '/dashboard/settings/security'},
            {'icon': '🎨', 'label': 'Preferences', 'href': '/dashboard/settings/preferences'}
        ]
    },
    {
        'icon': '👥',
        'label': 'Users',
        'href': '/dashboard/users',
        'children': [
            {'icon': '📝', 'label': 'Management', 'href': '/dashboard/users/management'},
            {'icon': '👑', 'label': 'Roles', 'href': '/dashboard/users/roles'},
            {'icon': '🔑', 'label': 'Permissions', 'href': '/dashboard/users/permissions'}
        ]
    }
]

BOTTOM_MENU = [
    {'icon': '❓', 'label': 'Help', 'href': '/help'},
    {'icon': '💭', 'label': 'Feedback', 'href': '/feedback'}
]
