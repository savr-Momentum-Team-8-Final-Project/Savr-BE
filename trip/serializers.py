from expenses.models import Expense
from rest_framework import serializers
from trip.models import Trip
from rest_framework.serializers import SerializerMethodField



class TripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [  
            'id',
            'trip_title',
            'city',
            'state',
            'start_date',
            'end_date',
            'guide',
            'budget'
            ]


class TripListSerializer(serializers.ModelSerializer):
    guide = SerializerMethodField()
    class Meta:
        model = Trip
        fields ='__all__'
    
    def get_guide(self,obj):
        return str(obj.guide.name)



    