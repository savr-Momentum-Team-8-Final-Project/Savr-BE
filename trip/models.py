from django.db import models
from django.conf import settings
from datetime import date


class Trip(models.Model):
    trip_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    guide = models.ForeignKey(User)

    def __str__(self):
        return self.trip_title

