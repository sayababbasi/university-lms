# backend/apps/users/views.py
# Basic placeholder views for the users app + (Developed by SAYAB)

from django.http import JsonResponse

def dummy_view(request):
    return JsonResponse({"message": "Users app is working"})
