from .models import Post, PostComment, PostImage, PostVideo
from notification.models import Notification
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
            
            Notification.objects.create(user=request.user, title='Your post has been successfully created')
            
            return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
class PostDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PostManagement(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        post.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)