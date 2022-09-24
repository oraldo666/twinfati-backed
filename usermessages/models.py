from django.db import models
from accounts.models import CustomUser

# Create your models here.


class UserMessages(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='message_sender')
    reciver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='message_reciver')
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sender.email


# class UserFriendship(models.Model):
#     user = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="logged_user")
#     friend = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="friends")

#     def __str__(self):
#         return self.user.email


# class UserFriendshipRequest(models.Model):
#     user = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="user_friendship_request")
#     friend = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="friend_friendship_request")
    
#     def __str__(self):
#         return self.user.email
