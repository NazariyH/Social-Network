from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import SignupForm 


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
            form.save()


            return Response({'message': 'Form Submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            message = 'Oops something went wrong :('

            for field in form:
                if field.errors:
                    for error in field.errors:
                        message = error
                        
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)