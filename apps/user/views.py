from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializer import UserCreateSerializer, JWTAuthenticationSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase


class JWTAuthenticationView(TokenViewBase):

    serializer_class = JWTAuthenticationSerializer
    permission_classes = [AllowAny]


class CreateUserView(CreateAPIView):

    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(data=request.data)
        return Response(headers=headers, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
