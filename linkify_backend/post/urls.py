from django.urls import path
from . import api

urlpatterns = [
    path('', api.PostList.as_view(), name='post-list'),
    path('create/', api.CreatePost.as_view(), name='create-post')
]