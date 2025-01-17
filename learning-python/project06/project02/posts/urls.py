from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostLikeToggleView, CommentUpdateView, CommentDeleteView


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