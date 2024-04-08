# prevetting_app/urls.py

from django.contrib import admin
from django.urls import path, include  # Ensure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inspections/', include('inspections.urls')),  # Include the inspections app's URLs
]
