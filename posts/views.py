from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import PostModel, PostLikeModel
from .serializers import PostSerializer, PostCreateSerializer, PostLikeSerializer, PostUpdateSerializer, PostUserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser, FormParser


from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from rest_framework.pagination import PageNumberPagination

# Create you views here.


class CustomPagination(PageNumberPagination):
    page_size = 10
    # page_size_query_param = 'page_size'
    # max_page_size = 3


class PostListCreateViewCustomPaginationView(PageNumberPagination):
    page_size = 15


class PostListCreateView(ListAPIView):
    queryset = PostModel.objects.order_by('-id')
    serializer_class = PostSerializer
    pagination_class = PostListCreateViewCustomPaginationView


class PostCreateView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    # parser_classes = (MultiPartParser, FormParser)

    # permission_classes = [IsAuthenticated]

    # def post(self, request, *args, **kwargs):
    #     request_user_id = request.data["user"]
    #     authenticate_user_id = self.request.user.id
    #     print(authenticate_user_id, request_user_id, "post create view")
    #     if int(request_user_id) != int(authenticate_user_id):
    #         print("User id does not match")
    #         return Response(request.data, status=status.HTTP_403_FORBIDDEN)
    #     print(request.data["user"], "Post create view")

    #     return self.create(request, *args, **kwargs)


class PostUpdateView(UpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostUpdateSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def like_post_view(request, pk):
    print(request.data['likes'])
    post = PostModel.objects.get(id=pk)
    post_like = PostLikeModel.objects.get(post_like_post=post)
    print(str(post_like) + ' Post like view')
    if request.method == 'PUT':
        if PostLikeModel.objects.filter(post_like_user=request.user):
            return Response("User alrady liked this post", status=status.HTTP_403_FORBIDDEN)
        else:
            post_like.post_like_user.add(request.user)
            post_like.save()
            user = request.user
            user_liking_this_post = post_like.post_like_user.all().count()
            post.likes = user_liking_this_post
            post.save()
            return Response("{} liked this post".format(request.user.first_name), status=status.HTTP_200_OK)


@api_view(['GET'])
def liked_by_user(request, pk):
    post = PostModel.objects.get(id=pk)
    post_like = PostLikeModel.objects.get(post_like_post=post)

    if PostLikeModel.objects.filter(post_like_user=request.user):
        data = {
            'liked': True
        }
        return Response(data, status=status.HTTP_200_OK)
    data = {
        'liked': False
    }
    return Response(data, status=status.HTTP_200_OK)


class GetUserPostsView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    # serializer_class = PostUserSerializer
    pagination_class = CustomPagination

    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        return PostModel.objects.filter(user=pk).order_by('-id')
