from rest_framework import serializers
from .models import LessonCompletion

class LessonCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonCompletion
        fields = ['id', 'user', 'lesson', 'completed_at']
