from django.urls import path
from .views import GetUserFriends, AddFriendsView, RemoveFriendsView

urlpatterns = [
    path('api/user/friends/', GetUserFriends.as_view()),
    path('api/add/friend/', AddFriendsView.as_view(), name='add-friend'),
    path('api/delete/friend/<int:pk>/',
         RemoveFriendsView.as_view(), name='remove-friend'),
]
