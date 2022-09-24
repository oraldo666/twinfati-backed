from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, CreateAPIView, DestroyAPIView
from .models import UserFriendship
from .serializers import UserFriendshipSerializer, AddFriendsSerializer

from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from django.shortcuts import get_object_or_404

# Create your views here.


class GetUserFriends(ListAPIView):
    queryset = UserFriendship.objects.all()
    serializer_class = UserFriendshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(self.request.user)
        return UserFriendship.objects.filter(user=user)[:10]


class AddFriendsView(CreateAPIView):
    queryset = UserFriendship.objects.all()
    serializer_class = AddFriendsSerializer
    permission_classes = [IsAuthenticated]


class RemoveFriendsView(DestroyAPIView):
    queryset = UserFriendship.objects.all()
    serializer_class = AddFriendsSerializer
