from rest_framework import viewsets
from .models import CourseEnrollment
from .serializers import CourseEnrollmentSerializer

class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer
