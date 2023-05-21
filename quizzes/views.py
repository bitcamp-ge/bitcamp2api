from rest_framework import viewsets
from .models import QuizAttempt
from .serializers import QuizAttemptSerializer

class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
