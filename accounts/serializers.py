from rest_framework import serializers
from .models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):


    class Meta():
        model = UserAccount
        fields = [ 
            'profile_pic',
        ]

