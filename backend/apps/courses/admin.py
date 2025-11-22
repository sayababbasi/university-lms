# apps/courses/admin.py
# Developed by SAYAB

from django.contrib import admin
from .models import Course, Module, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher", "created_at")
    search_fields = ("title", "teacher__user__username")

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    search_fields = ("title", "course__title")

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module")
    search_fields = ("title", "module__title")
