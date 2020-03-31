from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializer import UserCreateSerializer
from .models import User
from django.core.validators import ValidationError
from rest_framework import status
from rest_framework.response import Response


class CreateUserView(CreateAPIView):

    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def _perform_create(self, serializer):
        queryset = User.objects.filter(
            email=self.request.data['email']
        )

        if queryset.exists():
            raise ValidationError('User with given credentials already exist')

        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self._perform_create(serializer)
        headers = self.get_success_headers(data=request.data)
        return Response(headers=headers, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
