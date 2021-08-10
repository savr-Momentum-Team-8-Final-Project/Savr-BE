from rest_framework import serializers
from .models import UserAccount


class PhotoSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField()

    class Meta():
        model = UserAccount
        fields = [ 
            'profile_pic',
        ]


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserAccount
        fields = [
            "email",
            "name",
            "profile_pic"
        ]
