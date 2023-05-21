from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseEnrollmentViewSet

router = DefaultRouter()
router.register('enrollments', CourseEnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
