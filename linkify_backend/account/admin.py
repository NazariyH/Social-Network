from django.contrib import admin
from .models import User, Heshtag, SocialNetwork
# Register your models here.

admin.site.register(User)
admin.site.register(Heshtag)
admin.site.register(SocialNetwork)