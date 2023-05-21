from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonCompletionViewSet

router = DefaultRouter()
router.register('completions', LessonCompletionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
