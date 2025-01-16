import datetime
from django.shortcuts import render
from django.db import connection

def home(request):
    context = {
        'DEBUG_DATA': {
            'Request Info': {
                'method': request.method,
                'path': request.path,
                'GET params': dict(request.GET),
                'POST params': dict(request.POST),
            },
            'Performance': {
                'query_count': len(connection.queries),
                'query_time': sum(float(q['time']) for q in connection.queries),
            },
            'Custom Debug': {
                'my_variable': 'test value',
                'complex_data': {
                    'nested': ['list', 'of', 'items'],
                },
            },
        },
    }
    return render(request, 'home.html', context)


def dashboard(request):
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "user": {
            "id": 123,
            "username": "testuser",
            "email": "test@example.com",
        },
        "settings": {
            "theme": "dark",
            "language": "en",
        },
        "query_params": request.GET.dict(),
        "request_headers": dict(request.headers)
    }

    return render(request, 'dashboard.html', {'DEBUG_DATA': data})