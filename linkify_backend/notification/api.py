from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer

class NotificationGet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        notifications = get_list_or_404(Notification, user=request.user)
        serializer = NotificationSerializer(notifications, many=True)

        return Response({'notifications': serializer.data}, status=status.HTTP_200_OK)
    

class DeleteNotification(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        notification = get_object_or_404(Notification, pk=pk)
        notification.delete()

        notifications = get_list_or_404(Notification, user=request.user)
        serializer = NotificationSerializer(notifications, many=True)

        return Response({'notifications': serializer.data}, status=status.HTTP_200_OK)