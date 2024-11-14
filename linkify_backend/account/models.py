import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


# Create your models here.



class Heshtag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class SocialNetwork(models.Model):
    SOCIAL_MEDIA_CHOICE = [
        ('REDDIT', 'Reddit'),
        ('X', 'X'),
        ('TELEGRAM', 'Telegram'),
        ('INSTAGRAM', 'Instagram'),
    ]
    
    
    link = models.URLField(max_length=200, unique=True)
    media_type = models.CharField(
        max_length=20,
        choices=SOCIAL_MEDIA_CHOICE,
    )
    
    icon = models.ImageField(upload_to='social_network_icons/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        """ Automatically sets the icon based on media type if not provided. """
        
        icon_mapping = {
            'REDDIT': 'social_network_icons/reddit_icon.png',
            'X': 'social_network_icons/x_icon.png',
            'TELEGRAM': 'social_network_icons/telegram_icon.png',
            'INSTAGRAM': 'social_network_icons/instagram_icon.png',
        }
        
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.media_type


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', default='default_avatar.png', blank=True, null=True)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)], null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length='1000', null=True, blank=True)
    hashtags = models.ManyToManyField(Heshtag, related_name='users', null=True, blank=True)
    social_networks = models.ManyToManyField(SocialNetwork, related_name='users', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    data_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    