from django.urls import path
from .views import (
    PostListAPIView, 
    PostDetailAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    CommentListAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
    PostLikeToggleAPIView,

    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    PostLikeToggleView, 
    CommentUpdateView, 
    CommentDeleteView,
)


app_name = 'posts'

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post_list'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post-create/', PostCreateView.as_view(), name='post_create'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post-like/<int:pk>/', PostLikeToggleView.as_view(), name='post_like_toggle'),
    path('comment-update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]

urlpatterns += [
    path('api/', PostListAPIView.as_view(), name='api_post_list'),
    path('api/<int:pk>/', PostDetailAPIView.as_view(), name='api_post_detail'),
    path('api/create/', PostCreateAPIView.as_view(), name='api_post_create'),
    path('api/update/<int:pk>/', PostUpdateAPIView.as_view(), name='api_post_update'),
    path('api/delete/<int:pk>/', PostDeleteAPIView.as_view(), name='api_post_delete'),
    path('api/<int:post_id>/comments/', CommentListAPIView.as_view(), name='api_comment_list'),
    path('api/<int:post_id>/comments/create/', CommentCreateAPIView.as_view(), name='api_comment_create'),
    path('api/comments/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='api_comment_update'),
    path('api/comments/delete/<int:pk>/', CommentDeleteAPIView.as_view(), name='api_comment_delete'),
    path('api/<int:pk>/like/', PostLikeToggleAPIView.as_view(), name='api_post_like_toggle'),
]