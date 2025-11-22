# # backend/lms_crm/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse

# # --- Developed by SAYAB ---
# def root_view(request):
#     return HttpResponse("Welcome to University LMS Backend!")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', root_view, name='root'),  # <-- root URL
#     path('users/', include('apps.users.urls')),
#     path('courses/', include('apps.courses.urls')),
#     path('assignments/', include('apps.assignments.urls')),
#     path('attendance/', include('apps.attendance.urls')),
# ]


# backend/lms_crm/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# --- Developed by SAYAB ---
def root_api(request):
    """
    Root API view listing all available apps and their main endpoints.
    Useful for testing the backend during development.
    """
    data = {
        "message": "Welcome to University LMS Backend!",
        "endpoints": {
            "users": "/users/",
            "courses": "/courses/",
            "assignments": "/assignments/",
            "exams": "/exams/",
            "results": "/results/",
            "finance": "/finance/",
            "library": "/library/",
            "notifications": "/notifications/",
            "attendance": "/attendance/",
            "timetable": "/timetable/",
            "admin": "/admin/",
        }
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_api, name='root-api'),  # <-- root API
    path('users/', include('apps.users.urls')),
    path('courses/', include('apps.courses.urls')),
    path('assignments/', include('apps.assignments.urls')),
    path('exams/', include('apps.exams.urls')),
    path('results/', include('apps.results.urls')),
    path('finance/', include('apps.finance.urls')),
    path('library/', include('apps.library.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('timetable/', include('apps.timetable.urls')),
]
