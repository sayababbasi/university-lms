# apps/attendance/admin.py
# Developed by SAYAB

from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "status", "course")
    list_filter = ("date", "status", "course")
