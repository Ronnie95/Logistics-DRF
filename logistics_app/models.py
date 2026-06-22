from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    ROLE_CHOICES = (
        ("SUPERVISOR", "Supervisor"),
        ("DRIVER", "Driver "),
        ("ROUTER", "ROUTER"),
        ("MAINTENANCE", "MAINTENANCE"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.user.username
    
class Delivery(models.Model):
    stop = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    delivery_window = models.TimeField()
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    order_number = models.Random()
    status_choices = (
        ("IN ROUTE", "in route"),
        ("ARRIVED","ARRIVED"),
        ("COMPLETED", "COMPLETED"),
    )
    status = models.CharField(max_length=100, choices=status_choices)