from .models import Post, PostComment, PostImage, PostVideo
from rest_framework import serializers

from account.serializers import UserSerializer


class ImageSerialier(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['video']


class PostSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    author = UserSerializer(read_only=True)
    
    images = ImageSerialier(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'author',
            'likes_count',
            'comments_count',
            'is_liked',
            'created_at_formatted',
            'images',
            'videos',
        ]


    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            return user.is_authenticated and obj.likes.filter(id=user.id).exists()
        return False
