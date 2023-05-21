from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserLogout, UserViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')  # Register UserViewSet with the router


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('', include(router.urls)),  # Use router.urls
   
]