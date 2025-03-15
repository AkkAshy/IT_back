from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'prise', 'duration', 'course_type', 'certificate')
    list_filter = ('course_type', 'certificate')
    search_fields = ('title', 'teacher')