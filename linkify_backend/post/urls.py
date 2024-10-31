from django.urls import path
from . import api

urlpatterns = [
    path('', api.PostList.as_view(), name='post-list'),
]