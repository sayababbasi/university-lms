# # backend/lms_crm/views.py

# # Example view
# def home(request):
#     return JsonResponse({"message": "Welcome to University LMS"})
# backend/apps/assignments/views.py
# Developed by SAYAB
# backend/apps/assignments/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET

# Example view
@require_GET
def home(request):
    return JsonResponse({"message": "Welcome to University LMS"})
