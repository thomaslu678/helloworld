from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class FoodType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Entity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=15)
    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=15)
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    class Producer(models.Model):
        description = models.TextField()
        deliveries = models.IntegerField(default=0)
        usda_certified = models.BooleanField(null=True)
        image_link = models.TextField(blank=True)
        website_link = models.TextField(blank=True)

    class Volunteer(models.Model):
        deliveries = models.IntegerField(default=0)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    description = models.TextField()
    producer = models.ForeignKey(Entity.Producer, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    consumable = models.BooleanField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)


