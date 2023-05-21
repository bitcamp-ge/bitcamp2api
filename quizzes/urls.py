from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizAttemptViewSet

router = DefaultRouter()
router.register('attempts', QuizAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
