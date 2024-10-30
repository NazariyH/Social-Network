from django.urls import path
from . import api


urlpatterns = [
    path('notification/get/', api.NotificationGet.as_view(), name='get-notification'),
    path('notification/<int:pk>/delete/', api.DeleteNotification.as_view(), name='delete-notification')
]