from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions 
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import UserAccountSerializer


# Create your views here.
# 

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    ## request? format??
    def post(self, request, formart=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else: 
                if len(password) < 6:
                    return Response ({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email,password=password, name=name)

                    user.save()
                    return Response({'success': 'User created succesfully'})
        
        else:
            return Response ({'error': 'Passwords do not match'})




class UserAccountView(APIView):
    permission_classes = [permissions.AllowAny]
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
            file_serializer = UserAccountSerializer(data=request.data)
            if file_serializer.is_valid():
                    file_serializer.save()
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




