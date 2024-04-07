# blog/urls.py
from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView

urlpatterns = [
    path('post', PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:id>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
