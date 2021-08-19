from django.db.models.expressions import Value
from expenses.serializers import NoLinkExpenseListSerializer
from rest_framework import serializers
from trip.models import Trip
from expenses.models import Expense
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField
from django.db.models import Sum,Avg,Max,Min


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
            'budget',
            'c_photo',
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
    detail_url= trip_detail_url 
    delete_url = trip_delete_url 
    edit_url = trip_update_url
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
    total_expenses = SerializerMethodField()
    average_expenses = SerializerMethodField()
    max_expense = SerializerMethodField()
    budget_left = SerializerMethodField()
    lodging_expenses = SerializerMethodField()
    food_expenses = SerializerMethodField()
    trans_expenses = SerializerMethodField()
    ticket_expenses = SerializerMethodField()
    grocery_expenses = SerializerMethodField()
    other_expenses = SerializerMethodField()

    ### this can be negative
    
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
            'budget_left',
            'total_expenses',
            'average_expenses',
            'max_expense',
            'lodging_expenses',
            'food_expenses',
            'trans_expenses',
            'ticket_expenses',
            'grocery_expenses',
            'other_expenses',
            'expenses',
            'c_photo',
        ]

    def get_guide(self,obj):
        return str(obj.guide.name)

    def get_expenses(self,obj):
        e__qs = Expense.objects.filter(trip_id=obj.id)
        expenses = NoLinkExpenseListSerializer(e__qs, many=True).data
        return expenses

    def get_total_expenses(self,obj):
        e__qs = Expense.objects.filter(trip_id=obj.id)

        total_expenses = e__qs.aggregate(Sum('price'))
        return total_expenses

    def get_average_expenses(self,obj):
        e__qs = Expense.objects.filter(trip_id=obj.id)

        average_expenses = e__qs.aggregate(Avg('price'))
        return average_expenses

    def get_max_expense(self,obj):
        e__qs = Expense.objects.filter(trip_id=obj.id)

        max_expense = e__qs.aggregate(Max('price'))
        return max_expense


    def get_budget_left(self,obj):
        e__qs = Expense.objects.filter(trip_id=obj.id)
        total_expenses = e__qs.aggregate(Sum('price'))
        budget = obj.budget
        return budget-total_expenses.get('price__sum')


class TripUploadSerializer(serializers.ModelSerializer):

    class Meta():
        model = Trip
        fields = [
            "c_photo",
        ]




    def get_lodging_expenses(self,obj):
        l__qs = Expense.objects.filter(trip_id=obj.id).filter(category="lodging")
        lodging_expenses = l__qs.aggregate(Sum('price'))
        return lodging_expenses

    
    def get_food_expenses(self,obj):
        f__qs = Expense.objects.filter(trip_id=obj.id).filter(category="food")
        food_expenses = f__qs.aggregate(Sum('price'))
        return food_expenses


    def get_trans_expenses(self,obj):
        t__qs = Expense.objects.filter(trip_id=obj.id).filter(category="trans")
        trans_expenses = t__qs.aggregate(Sum('price'))
        return trans_expenses

    def get_ticket_expenses(self,obj):
        t__qs = Expense.objects.filter(trip_id=obj.id).filter(category="ticket")
        ticket_expenses = t__qs.aggregate(Sum('price'))
        return ticket_expenses

    def get_grocery_expenses(self,obj):
        g__qs = Expense.objects.filter(trip_id=obj.id).filter(category="grocery")
        grocery_expenses = g__qs.aggregate(Sum('price'))
        return grocery_expenses


    def get_other_expenses(self,obj):
        o__qs = Expense.objects.filter(trip_id=obj.id).filter(category="other")
        other_expenses = o__qs.aggregate(Sum('price'))
        return other_expenses






