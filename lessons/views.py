from rest_framework import viewsets
from .models import LessonCompletion
from .serializers import LessonCompletionSerializer

class LessonCompletionViewSet(viewsets.ModelViewSet):
    queryset = LessonCompletion.objects.all()
    serializer_class = LessonCompletionSerializer
