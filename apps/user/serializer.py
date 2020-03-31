from .models import User
from rest_framework import serializers
from rest_framework import validators


class UserCreateSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass
