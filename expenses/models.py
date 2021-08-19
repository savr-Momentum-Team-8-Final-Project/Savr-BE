from django.db import models
from accounts.models import UserAccount
from django.db.models.deletion import CASCADE
from trip.models import Trip
from datetime import date

# Create your models here.
class Expense(models.Model):
    expense_title = models.CharField(max_length=100, null = True)
    ## upload file start ** 
    file =  models.FileField(upload_to='media/', null=True, blank=True,)

    content = models.TextField(blank=True)
    ###  upload file end ** 

    price = models.DecimalField(max_digits=6, decimal_places= 2, null=True, default=0.00)
    note = models.TextField(blank=True)
    trip = models.ForeignKey(Trip, on_delete=CASCADE)
    date = models.DateField(blank=True, null=True)
    ## category drop down menu
    CATEGORY_CHOICES= [
        ('lodging', 'Lodging'),
        ('food', 'Food'),
        ('trans', 'transportation'),
        ('ticket', 'Ticket'), 
        ('grocery', 'Grocery'),
        ('other', 'Other'),
    ]
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES
    )
