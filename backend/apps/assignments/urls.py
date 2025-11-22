# backend/apps/assignments/urls.py
# User app URLs (basic placeholder to avoid empty urlpatterns) + (Developed by SAYAB)

# backend/apps/assignments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dummy_view, name='assignments-home'),
]
