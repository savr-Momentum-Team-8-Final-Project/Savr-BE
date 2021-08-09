from expenses.serializers import NoLinkExpenseListSerializer
from rest_framework import serializers
from trip.models import Trip
from rest_framework.serializers import SerializerMethodField
from expenses.models import Expense



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

    
class TripDetailSerialzier(serializers.ModelSerializer):
    guide = SerializerMethodField()
    expenses = SerializerMethodField()
    
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
            'budget',
            'expenses',
        ]

    def get_guide(self,obj):
        return str(obj.guide.name)

    def get_expenses(self,obj):
        e__qs = Expense.objects.filter(trip_id=obj.id)
        expenses = NoLinkExpenseListSerializer(e__qs, many=True).data
        return expenses





