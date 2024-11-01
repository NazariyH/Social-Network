from .models import Post, PostComment, PostImage, PostVideo
from rest_framework import serializers

from account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'likes_count', 'comments_count', 'is_liked', 'created_at_formatted']


    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            return user.is_authenticated and obj.likes.filter(id=user.id).exists()
        return False
