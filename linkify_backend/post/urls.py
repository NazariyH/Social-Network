from django.urls import path
from . import api

urlpatterns = [
    path('', api.PostList.as_view(), name='post-list'),
    path('create/', api.CreatePost.as_view(), name='create-post'),
    path('<uuid:pk>/delete/', api.PostManagement.as_view(), name='post-management'),
    path('<uuid:pk>/detail/', api.PostDetail.as_view(), name='post-detail'),
]