from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from logging import warning

from .models import User



class JWTAuthenticationSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        authenticate_credentials = {
            "email": attrs["email"],
            "password": attrs["password"]
        }

        user = authenticate(request=self.context["request"], **authenticate_credentials)




class UserCreateSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True)

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user.exists():
            raise serializers.ValidationError("User with given credentials already exist")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        pass
