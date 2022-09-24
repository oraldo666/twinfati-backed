from django.urls import path
from .views import PostListCreateView, PostCreateView, PostUpdateView, like_post_view, liked_by_user, GetUserPostsView


urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/like/<int:pk>/', like_post_view),
    path('post/update/<int:pk>/', PostUpdateView.as_view()),
    path('post/user/like/<int:pk>/', liked_by_user),
    path('post/user/search/<int:pk>/',
         GetUserPostsView.as_view(), name="get_user_posts")
]
