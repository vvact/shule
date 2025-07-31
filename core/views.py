# core/views.py
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Welcome to the Shule API 🚀</h1>
        <p>This is the backend for Shule. Use <a href="/api/">/api/</a> to access the API.</p>
    """)

