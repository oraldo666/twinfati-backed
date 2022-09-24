from django.db import models
from django.utils import timezone, dateformat
from datetime import datetime
from accounts.models import CustomUser


# Create your models here.

class PostModel(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name="user", on_delete=models.CASCADE)
    post_text = models.TextField(max_length=10000, blank=True, null=True)
    post_img = models.ImageField(blank=True, null=True, upload_to='posts')
    likes = models.IntegerField(default=0)
    liked_or_not = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    modified = models.DateTimeField(editable=False, null=True, blank=True)
    post_user_likes = models.ManyToManyField(
        CustomUser, blank=True, related_name='post_user_likes')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = dateformat.format(datetime.now(), 'Y-m-d H:i:s')
        self.modified = dateformat.format(datetime.now(), 'Y-m-d H:i:s')
        return super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post Model'

    def __str__(self):
        return self.post_text


class PostLikeModel(models.Model):
    post_like_post = models.OneToOneField('PostModel',
                                          related_name='post_like_post_key',
                                          on_delete=models.CASCADE,
                                          )
    post_like_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="post_like_user_key",
        blank=True,
        null=True
    )
    post_like_date = models.DateTimeField(
        dateformat.format(datetime.now(), 'Y-m-d H:i:s'), null=True, blank=True)

    def __str__(self):
        return str(self.post_like_post)


class PostComment(models.Model):
    comment_post = models.OneToOneField('PostModel',
                                        related_name='comment_post_key',
                                        on_delete=models.CASCADE
                                        )
    comment_author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="comment_author_key"
    )
    comment_text = models.TextField()
    comment_created_date = models.DateTimeField(
        dateformat.format(datetime.now(), 'Y-m-d H:i:s'), null=True, blank=True
    )
