# backend/apps/attendance/urls.py
# URL patterns for Attendance app (placeholder) + (Developed by SAYAB)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dummy_view, name='attendance-home'),
]
