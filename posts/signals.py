from .models import PostModel, PostLikeModel

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=PostModel)
def create(sender, instance, created, **kwargs):
    if created:
        PostLikeModel.objects.create(
            post_like_post=instance,
        )

    print('Post created !!!')


@receiver(post_save, sender=PostLikeModel)
def create_field(sender, instance, **kwargs):
    post_like = PostModel.objects.get(id=instance.post_like_post.id)
    post_like.post_user_likes.add(instance.post_like_user)

    print(instance.post_like_post.id)
    return
