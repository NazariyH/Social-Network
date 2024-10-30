from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title