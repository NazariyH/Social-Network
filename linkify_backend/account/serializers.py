from rest_framework import serializers
from .models import User, Heshtag, SocialNetwork


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heshtag
        fields = ['name']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['link', 'media_type', 'icon']
        

class UserSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(read_only=True, many=True)
    social_networks = SocialMediaSerializer(read_only=True, many=True)
    is_current_user = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 
            'name', 
            'email', 
            'avatar', 
            'age', 
            'origin', 
            'bio',
            'hashtags',
            'social_networks',
            'is_current_user',
        ]
        
    def get_is_current_user(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            return user.is_authenticated and obj == user
        return False
