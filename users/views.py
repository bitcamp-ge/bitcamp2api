from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication



class UserLogout(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        token, created = Token.objects.get_or_create(user=serializer.instance)
        data = serializer.data
        data["token"] = token.key
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

