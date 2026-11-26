from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'register_number',
        'full_name',
        'email',
        'phone',
        'department',
        'course',
    )

    search_fields = (
        'register_number',
        'full_name',
        'email',
    )

    list_filter = (
        'department',
        'course',
    )

    ordering = ('register_number',)