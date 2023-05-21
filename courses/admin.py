from django.contrib import admin
from .models import Course, CourseEnrollment

admin.site.register(Course)
admin.site.register(CourseEnrollment)