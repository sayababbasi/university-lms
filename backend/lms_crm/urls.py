# # backend/lms_crm/urls.py
# # Root URL configuration + (Developed by SAYAB)

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/users/', include('apps.users.urls')),
#     path('api/courses/', include('apps.courses.urls')),
#     path('api/assignments/', include('apps.assignments.urls')),
#     path('api/exams/', include('apps.exams.urls')),
#     path('api/results/', include('apps.results.urls')),
#     path('api/finance/', include('apps.finance.urls')),
#     path('api/notifications/', include('apps.notifications.urls')),
#     path('api/attendance/', include('apps.attendance.urls')),
#     path('api/timetable/', include('apps.timetable.urls')),
#     path('api/library/', include('apps.library.urls')),
# ]


# File: backend/lms_crm/urls.py
# Main URL configuration for the University LMS project + (Developed by SAYAB)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('courses/', include('apps.courses.urls')),
    path('assignments/', include('apps.assignments.urls')),
    path('attendance/', include('apps.attendance.urls')),
]
