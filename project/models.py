from django.db import models
from django.utils import timezone

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(
                         max_digits = 20,
                         decimal_places = 15)
    longitude = models.DecimalField(
                         max_digits = 20,
                         decimal_places = 15)
    date_posted = models.DateTimeField(default=timezone.now)