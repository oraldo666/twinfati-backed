from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, CreateAPIView, DestroyAPIView
from .models import UserMessages
from .serializers import MessageSerializer

from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from django.shortcuts import get_object_or_404

# Create your views here.


class GetMessageView(ListAPIView):
    queryset = UserMessages.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        sender = self.request.user
        pk = self.kwargs['pk']
        print(self.request.user)

        return UserMessages.objects.filter(Q(Q(sender=sender) | Q(sender=pk)), Q(Q(reciver=pk) | Q(reciver=sender))).order_by('id')


class GetFriendMessages(ListAPIView):
    queryset = UserMessages.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        friend = self.kwargs['pk']
        user = self.request.user
        return UserMessages.objects.filter(sender=friend, reciver=user)


# class GetUserFriends(ListAPIView):
#     queryset = UserFriendship.objects.all()
#     serializer_class = UserFriendshipSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         print(self.request.user)
#         return UserFriendship.objects.filter(user=user)[:10]


# class AddFriendsView(CreateAPIView):
#     queryset = UserFriendship.objects.all()
#     serializer_class = AddFriendsSerializer
#     permission_classes = [IsAuthenticated]


# class RemoveFriendsView(DestroyAPIView):
#     queryset = UserFriendship.objects.all()
#     serializer_class = AddFriendsSerializer
