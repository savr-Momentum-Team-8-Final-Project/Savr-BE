from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError
from rest_framework.generics import RetrieveUpdateAPIView
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, serializers
from rest_framework.parsers import (
    FileUploadParser,
)

from rest_framework import status
from .serializers import UserAccountSerializer
from .models import UserAccount



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
    parser_classes = [FileUploadParser]
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        user = request.user
        if "file" in request.data:
            file=request.data["file"]
            user.profile_pic.save(file.name, file, save=True)

        serializer = UserAccountSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




