from django.db import models
from django.conf import settings
from datetime import date
from django.db.models.deletion import CASCADE
from accounts .models import UserAccount


class Trip(models.Model):
    trip_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    guide = models.ForeignKey(UserAccount, on_delete=CASCADE)
    budget = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    
    def __str__(self):
        return self.trip_title

