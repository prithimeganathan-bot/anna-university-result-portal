from django.contrib import admin
from .models import Student, SubjectResult

# This allows adding students/results from Django admin panel
class SubjectResultInline(admin.TabularInline):
    model = SubjectResult
    extra = 6  # Show 6 subject rows by default

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['register_number', 'name', 'department', 'semester']
    inlines = [SubjectResultInline]  # Show subjects inside student page

@admin.register(SubjectResult)
class SubjectResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject_code', 'subject_name', 'grade', 'result']

# Register your models here.
