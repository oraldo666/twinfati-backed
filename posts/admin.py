from django.contrib import admin
from .models import PostModel, PostLikeModel, PostComment

# Register your models here.

admin.site.register(PostModel)
admin.site.register(PostLikeModel)
admin.site.register(PostComment)
