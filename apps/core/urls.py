#core urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
# Note: The views home, about, and contact should be defined in apps/core/views.py
