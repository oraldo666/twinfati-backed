from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializer, UserDeeatilsSerializer, ImageSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.pagination import PageNumberPagination

# Function based view imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
# Create you views here.


class CustomPagination(PageNumberPagination):
    page_size = 7
    # page_size_query_param = 'page_size'
    # max_page_size = 3


class RegisterUser(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDeeatilsSerializer
    permission_classes = [IsAuthenticated]


class SearchedUserDetailsView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDeeatilsSerializer


class SearchUserView(ListAPIView):
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = UserDeeatilsSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']


class UpdateProfilePhoto(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ImageSerializer

    def get_object(self):
        user_query = CustomUser.objects.get(id=self.request.user.id)
        return user_query

    def put(self, request, *args, **kwargs):
        current_user = CustomUser.objects.get(id=self.request.user.id)
        current_user.profile_photo = self.request.data["img"]
        current_user.save()
        return self.update(request, *args, **kwargs)
