# backend/apps/finance/urls.py
# User app URLs (basic placeholder to avoid empty urlpatterns) + (Developed by SAYAB)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dummy_view, name='finance-home'),
]
