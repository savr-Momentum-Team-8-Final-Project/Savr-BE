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
            'price',
            'note',
            'date',
            'category',
        ]


class UploadReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = [
            'file',
            'content',
        ]



class ExpenseDetailSerializer(serializers.ModelSerializer):
### turn users to show name 
    ### receipt
    user = SerializerMethodField()
    class Meta:
        model = Expense
        fields = [
            'id',
            'user',
            'trip',
            'file',
            'expense_title',
            "price",
            'category',
            'note',
            'date',
            
        ]
    
    def get_user(self,obj):
        return str(obj.trip.guide.name)

    


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

    
    class Meta:
        model = Expense
        fields = [
            'id',
            'expense_title',
            'file',
            'price',
            'category',
            'date',
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




class UpdateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'expense_title',
            'trip', 
            'file',
            'price',
            'note',
            'date',
            'category',
        ]



##### list of expenses without links ***** 
class NoLinkExpenseListSerializer(serializers.ModelSerializer):

    user = SerializerMethodField()
    trip_name = SerializerMethodField()
    
    class Meta:
        model = Expense
        fields = [
            'id',
            'expense_title',
            'file',
            'price',
            'category',
            'user',
            'trip', 
            'trip_name',
            
        ]

    def get_user(self,obj):
        return str(obj.trip.guide.name)
    
    def get_trip_name(self,obj):
        return str(obj.trip.trip_title)