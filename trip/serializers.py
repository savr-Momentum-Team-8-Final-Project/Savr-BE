from expenses.serializers import NoLinkExpenseListSerializer
from rest_framework import serializers
from trip.models import Trip
from expenses.models import Expense
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField



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

trip_detail_url = HyperlinkedIdentityField(
        view_name='trip_detail',
        lookup_field='pk'
    )

trip_delete_url = HyperlinkedIdentityField(
        view_name='trip_delete',
        lookup_field='pk'
    )

trip_update_url = HyperlinkedIdentityField(
        view_name='trip_update',
        lookup_field='pk',
    )


class TripListSerializer(serializers.ModelSerializer):
    guide = SerializerMethodField()
    class Meta:
        model = Trip
        fields ='__all__'

    def get_guide(self,obj):
        return str(obj.guide.name)

class TripUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'trip_title',
            'city', 
            'state',
            'start_date',
            'end_date',
            'guide',
            'budget',
        ]



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










