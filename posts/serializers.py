from rest_framework import serializers
from .models import PostModel, PostLikeModel, PostComment
from accounts.models import CustomUser
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "profile_photo", 'id']


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class PostLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikeModel
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'

# , allow_empty_file=True, use_url=True


class PostCreateSerializer(serializers.ModelSerializer):
    post_img = serializers.ImageField(
        required=False, max_length=None, allow_null=True)

    class Meta:
        model = PostModel
        fields = ['post_img', 'post_text', 'user']

    def create(self, validated_data):
        # instance.post_img = validated_data.get('post_img', instance.post_img)
        # instance.post_text = validated_data.get(
        #     'post_text', instance.post_text)
        # instance.user = validated_data.get('user', instance.user)
        return PostModel.objects.create(**validated_data)


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['post_img', 'post_text', 'user']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['likes']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    isMine = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ['id', 'post_img', 'post_text',
                  'user', 'likes', 'isMine']

    def get_isMine(self, obj):
        requestUser = self.context['request'].user
        current_post = PostModel.objects.get(id=obj.id)
        users_liked = current_post.post_user_likes.all()
        for user_liked in users_liked:
            if user_liked.email == requestUser.email:
                print(str(user_liked) + ' True')
                return True
