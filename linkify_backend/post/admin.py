from django.contrib import admin
from .models import Post, PostImage, PostComment, PostVideo

# Register your models here.

admin.site.register(Post)

admin.site.register(PostImage)

admin.site.register(PostVideo)

admin.site.register(PostComment)
