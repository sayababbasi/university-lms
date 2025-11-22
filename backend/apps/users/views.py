# backend/apps/users/views.py
from django.http import HttpResponse

# --- Developed by SAYAB ---
def home_view(request):
    return HttpResponse("Users Home Page")
