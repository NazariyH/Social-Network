from uuid import uuid4

from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.timesince import timesince

from account.models import User


# Create your models here.
MAX_VIDEO_SIZE = 25 * 1024 * 1024 # 25mb
MAX_IMAGE_SIZE = 7 * 1024 * 1024 # 7mb


def validate_video_size(value):
    if value.size > MAX_VIDEO_SIZE:
        raise ValidationError(f'The maximum file size is {MAX_VIDEO_SIZE / (1024 * 1024)} MB')
    
def validate_image_size(value):
    if value.size > MAX_IMAGE_SIZE:
        raise ValidationError(f'The maximum file size is {MAX_IMAGE_SIZE / (1024 * 1024)} MB')



class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=3000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    likes_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.likes_count = self.likes.count()
        super().save(*args, **kwargs)
        
    def created_at_formatted(self):
        return timesince(self.created_at)
        



class PostImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='post/images/', 
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_image_size,
        ]
    )


    def __str__(self):
        return self.post.title



class PostVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(
        upload_to='post/videos/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4']),
            validate_video_size,
        ]
    )

    
    def __str__(self):
        return self.post.title
    

class PostComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    likes_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.body
    
    def save(self, *args, **kwargs):
        self.likes_count = self.likes.count()
        super().save(*args, **kwargs)