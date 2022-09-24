from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

from django.forms.fields import ImageField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', "first_name",
                  "last_name", "profile_photo", "password"]

    def validate_password(self, password: str) -> str:
        return make_password(password)


class UserDeeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "last_login", "date_joined", "email",
                  "first_name", "last_name",   "profile_photo"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_photo']
