from django.urls import path
from .views import RegisterUser, UserDetailsView, SearchUserView, SearchedUserDetailsView, UpdateProfilePhoto
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

from .customtoken import MyTokenObtainPairView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/register/', RegisterUser.as_view(), name='register_user'),
    path('api/user/details/<int:pk>/',
         UserDetailsView.as_view(), name='user_details'),
    path('api/user/search', SearchUserView.as_view(), name='search_user'),
    path('api/user/search/profile/<int:pk>/',
         SearchedUserDetailsView.as_view(), name='profile_search'),
    path('api/user/profile-photo/',
         UpdateProfilePhoto.as_view(), name="profile_photo"),
]
