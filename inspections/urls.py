# inspections/urls.py
from django.urls import path
from .views import list_inspections, create_inspection

urlpatterns = [
    path('', list_inspections, name='list_inspections'),
    path('create/', create_inspection, name='create_inspection'),
]