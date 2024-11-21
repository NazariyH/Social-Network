from django.urls import path
from . import api

urlpatterns = [
    path('', api.PostList.as_view(), name='post-list'),
    path('create/', api.CreatePost.as_view(), name='create-post'),
    path('<uuid:pk>/delete/', api.PostManagement.as_view(), name='post-delete'),
    path('<uuid:pk>/hide-toggle/', api.PostManagement.as_view(), name='post-hide-toggle'),
    path('<uuid:pk>/detail/', api.PostDetail.as_view(), name='post-detail'),
]