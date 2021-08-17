import trip
from rest_framework import serializers
from .models import UserAccount
from rest_framework.serializers import SerializerMethodField
from expenses.models import Expense,Trip
from django.db.models import Sum,Avg,Max,Min

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserAccount
        fields = [
            "email",
            "name",
            "profile_pic",
        ]



class UserSummarySerializer(serializers.ModelSerializer):

    alltrip_expenses = SerializerMethodField()
    alltrip_avg = SerializerMethodField()
    alltrip_max = SerializerMethodField()
    total_budget = SerializerMethodField()
    average_budget = SerializerMethodField()
    trip_count = SerializerMethodField()
    class Meta():
        model = UserAccount
        fields = [
            "id", 
            "email",
            "name",
            "alltrip_expenses",
            'alltrip_avg', 
            'alltrip_max',
            'total_budget',
            'average_budget',
            'trip_count',
        ]

    def get_alltrip_expenses(self,obj):
        ### I like this part!!!
        e__qs = Expense.objects.filter(trip__guide_id=obj.id)

        alltrip_expenses = e__qs.aggregate(Sum('price'))
        return alltrip_expenses


    def get_alltrip_avg(self,obj):
        ### I like this part!!!
        e__qs = Expense.objects.filter(trip__guide_id=obj.id)

        alltrip_avg = e__qs.aggregate(Avg('price'))
        return alltrip_avg

    
    def get_alltrip_max(self,obj):
        ### I like this part!!!
        e__qs = Expense.objects.filter(trip__guide_id=obj.id)

        alltrip_max = e__qs.aggregate(Max('price'))
        return alltrip_max
    
    def get_total_budget(self,obj):
        ### I like this part!!!
        b__qs = Trip.objects.filter(guide_id=obj.id)

        total_budget = b__qs.aggregate(Sum('budget'))
        return total_budget


    def get_average_budget(self,obj):
        ### I like this part!!!
        b__qs = Trip.objects.filter(guide_id=obj.id)

        average_budget = b__qs.aggregate(Avg('budget'))
        return average_budget

    
    def get_trip_count(self,obj):
        ### I like this part!!!
        b__qs = Trip.objects.filter(guide_id=obj.id)
        return b__qs.count()