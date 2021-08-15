from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField

from .models import Expense


class ExpenseUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = [
            'trip',
            'file',
        ]


class ExpenseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = [
            'expense_title',
            'trip', 
            'file',
            'amount',
            'price',
            'note',
            'date',
            'category',
        ]

        #### user is read only!! 

class ExpenseDetailSerializer(serializers.ModelSerializer):
### turn users to show name 
    user = SerializerMethodField()
    total_cost = SerializerMethodField()
    class Meta:
        model = Expense
        fields = [
            'id',
            'user',
            'trip',
            'expense_title',
            "amount",
            "price",
            'total_cost',
            'category',
            'note',
            'date',
            
        ]
    
    def get_user(self,obj):
        return str(obj.trip.guide.name)


    def get_total_cost(self,obj):
        return obj.amount * obj.price
    


## url
expense_detail_url = HyperlinkedIdentityField(
        view_name='expense_detail',
        lookup_field='pk'
    )

### delete url
expense_delete_url = HyperlinkedIdentityField(
        view_name='expense_delete',
        lookup_field='pk'
    )

### edit url 
expense_edit_url = HyperlinkedIdentityField(
        view_name='expense_update',
        lookup_field='pk',
    )



class ExpenseListSerializer(serializers.ModelSerializer):
    detail_url= expense_detail_url 
    delete_url = expense_delete_url 
    edit_url = expense_edit_url
    user = SerializerMethodField()
    trip_name = SerializerMethodField()
    total_cost = SerializerMethodField()

    
    class Meta:
        model = Expense
        fields = [
            'id',
            'expense_title',
            'amount',
            'price',
            'total_cost', 
            'category',
            'user',
            'trip', 
            'trip_name',
            'detail_url',
            'delete_url',
            'edit_url',
        ]

    def get_user(self,obj):
        return str(obj.trip.guide.name)
    
    def get_trip_name(self,obj):
        return str(obj.trip.trip_title)

    def get_total_cost(self,obj):
        return obj.amount * obj.price




class UpdateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'expense_title',
            'trip', 
            'amount',
            'price',
            'note',
            'date',
            'category',
        ]



##### list of expenses without links ***** 
class NoLinkExpenseListSerializer(serializers.ModelSerializer):

    user = SerializerMethodField()
    trip_name = SerializerMethodField()
    total_cost = SerializerMethodField()
    
    class Meta:
        model = Expense
        fields = [
            'id',
            'expense_title',
            'amount',
            'price',
            'total_cost', 
            'category',
            'user',
            'trip', 
            'trip_name',
        ]

    def get_user(self,obj):
        return str(obj.trip.guide.name)
    
    def get_trip_name(self,obj):
        return str(obj.trip.trip_title)

    def get_total_cost(self,obj):
        return obj.amount * obj.price
