# materials/urls.py
from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.material_filter_view, name='material_filter'),
]
