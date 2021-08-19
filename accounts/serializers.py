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
    alltrip_lodging = SerializerMethodField()
    alltrip_food = SerializerMethodField()
    alltrip_trans = SerializerMethodField()
    alltrip_ticket = SerializerMethodField()
    alltrip_grocery = SerializerMethodField()
    alltrip_other = SerializerMethodField()
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
            "alltrip_lodging",
            "alltrip_food",
            "alltrip_trans",
            "alltrip_ticket",
            "alltrip_grocery",
            "alltrip_other",
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



    def get_alltrip_lodging(self,obj):
        l__qs = Expense.objects.filter(trip__guide_id=obj.id).filter(category="lodging")
        alltrip_lodging = l__qs.aggregate(Sum('price'))
        return alltrip_lodging
    
    def get_alltrip_food(self,obj):
        f__qs = Expense.objects.filter(trip__guide_id=obj.id).filter(category="food")
        alltrip_food= f__qs.aggregate(Sum('price'))
        return alltrip_food



    def get_alltrip_trans(self,obj):
        t__qs = Expense.objects.filter(trip__guide_id=obj.id).filter(category="trans")
        alltrip_trans= t__qs.aggregate(Sum('price'))
        return alltrip_trans



    def get_alltrip_ticket(self,obj):
        t__qs = Expense.objects.filter(trip__guide_id=obj.id).filter(category="ticket")
        alltrip_ticket= t__qs.aggregate(Sum('price'))
        return alltrip_ticket


    def get_alltrip_grocery(self,obj):
        g__qs = Expense.objects.filter(trip__guide_id=obj.id).filter(category="grocery")
        alltrip_grocery= g__qs.aggregate(Sum('price'))
        return alltrip_grocery


    def get_alltrip_other(self,obj):
        g__qs = Expense.objects.filter(trip__guide_id=obj.id).filter(category="other")
        alltrip_other= g__qs.aggregate(Sum('price'))
        return alltrip_other

    
