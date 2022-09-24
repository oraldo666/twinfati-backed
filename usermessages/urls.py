from django.urls import path
from .views import GetMessageView,  GetFriendMessages

urlpatterns = [
    path('api/message/<int:pk>/', GetMessageView.as_view(), name='message_list'),
    path('api/friend/message/<int:pk>/',
         GetFriendMessages.as_view(), name='friend-message-list'),
    #     path('api/user/friends/', GetUserFriends.as_view()),
    #     path('api/add/friend/', AddFriendsView.as_view(), name='add-friend'),
    #     path('api/delete/friend/<int:pk>/',
    #          RemoveFriendsView.as_view(), name='remove-friend'),
]
