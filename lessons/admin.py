from django.contrib import admin
from .models import Lesson, LessonCompletion

admin.site.register(Lesson)
admin.site.register(LessonCompletion)