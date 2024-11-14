from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import SignupForm 
from notification.models import Notification
from .models import User
from .serializers import UserSerializer


class Signup(APIView):
    authentication_classes = []
    permission_classes = [] 


    def post(self, request, *args, **kwargs):
        data = request.data

        form = SignupForm({
            'email': data.get('email'),
            'name': data.get('name'),
            'password': data.get('password1'),
            'password1': data.get('password1'),
            'password2': data.get('password2'),
        })

        if form.is_valid():
            user = form.save()

            Notification.objects.create(user=user, title='Your account has been successfully created')
            return Response({'message': 'Form Submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            message = 'Oops something went wrong :('

            for field in form:
                if field.errors:
                    for error in field.errors:
                        message = error
                        
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
        


class Me(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
        }, status=status.HTTP_200_OK)
        
        
class Profile(APIView):
    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, id=pk)
        profileSerializer = UserSerializer(user, context={'request': request})
        
        return Response({'profile': profileSerializer.data}, status=status.HTTP_200_OK)