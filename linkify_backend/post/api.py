from .models import Post, PostComment, PostImage, PostVideo
from .serializers import PostSerializer
from .forms import PostForm

from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class PostList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        post_list = get_list_or_404(Post)

        serializer = PostSerializer(post_list, many=True, context={'request': request})

        return Response({'post_list': serializer.data}, status=status.HTTP_200_OK)


class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        print(images)  
            
        form = PostForm(request.data)
        
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            serializer = PostSerializer(post)
            
            images = request.FILES.getlist('images')
            print(images)
            for image in images:
                PostImage.objects.create(post=post, image=image)
                
            videos = request.FILES.getlist('videos')
            for video in videos:
                PostVideo.objects.create(post=post, video=video)
            
            
            
            return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': form.errors}, status=status.HTTP_400_BAD_REQUEST)