from rest_framework import serializers
from .models import CourseEnrollment

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = ['id', 'user', 'course', 'enrolled_at']