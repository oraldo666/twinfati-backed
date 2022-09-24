from rest_framework import serializers
from .models import UserMessages
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "profile_photo", 'id']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessages
        fields = '__all__'


# class UserFriendshipSerializer(serializers.ModelSerializer):
#     friend = UserSerializer(read_only=True)

#     class Meta:
#         model = UserFriendship
#         fields = '__all__'


# class AddFriendsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserFriendship
#         fields = '__all__'
