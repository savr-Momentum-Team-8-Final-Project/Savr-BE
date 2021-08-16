from django.db import models
from accounts.models import UserAccount
from django.db.models.deletion import CASCADE
from trip.models import Trip
from datetime import date

# Create your models here.
class Expense(models.Model):
    expense_title = models.CharField(max_length=100, null = True)
    amount = models.IntegerField(default=1)
    ## upload file start ** 
    file =  models.FileField(upload_to='media/', null=True, blank=True,)
    ###  upload file end ** 

    price = models.DecimalField(max_digits=6, decimal_places= 2, null=True)
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


    def __str__(self):
        return self.expense_title

### this is for file upload
    def __str__(self):
        return self.file.name