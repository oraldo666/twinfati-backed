from django.contrib import admin
from .models import UserFriendship, UserFriendshipRequest
# Register your models here.

admin.site.register(UserFriendship)
admin.site.register(UserFriendshipRequest)
