# backend/apps/users/urls.py
from django.urls import path
from . import views

# --- Developed by SAYAB ---
urlpatterns = [
    path('', views.home_view, name='users-home'),  # replace with actual view
]
