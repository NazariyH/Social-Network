from .models import Post, PostComment, PostImage, PostVideo
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import PostSerializer



class PostList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        post_list = get_list_or_404(Post)

        serializer = PostSerializer(post_list, many=True)

        return Response({'post_list': serializer.data}, status=status.HTTP_200_OK)

