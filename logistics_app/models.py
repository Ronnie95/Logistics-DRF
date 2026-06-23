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
    


class Truck(models.Model):
    truck_number = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField
    truck_choices = (
        ("FLAT BED", "flat bed"),
        ("DAY CAB", "day cab"),
        ("SINGLE CAB", "single cab")
    )
    truck_options = models.CharField(max_length=50, choices=truck_choices)

class Trailer(models.Model):
    trailer_number = models.IntegerField()
    trailer_choices = (
        ("28 FT", "28 ft"),
        ("53 FT", "53 ft"),
    )
    trailer_option = models.CharField(max_length=20, choices=trailer_choices)

class Routes(models.Model): #add permissions assigned_to after enpoint testing 
    route_name = models.CharField(max_length=100)
    route_date = models.DateField()
    trucks = models.ForeignKey(Truck, on_delete= models.CASCADE)
    trailers = models.ForeignKey(Trailer, on_delete= models.CASCADE)

    #driver permissions will be added once tested


class CustomerInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    
class Delivery(models.Model):
    routes = models.ForeignKey(Routes, on_delete=models.CASCADE, related_name= "deliveries")
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    order_number = models.Random()
    status_choices = (
        ("IN ROUTE", "in route"),
        ("ARRIVED","ARRIVED"),
        ("COMPLETED", "COMPLETED"),
    )
    status = models.CharField(max_length=100, choices=status_choices)
    delivered_at = models.DateTimeField()

class DeliverExceptions(models.CharField):
    exception_choices = (
        ("NO_HOME", "Cstomer not home"),
        ("BAD_ADDRESS", "Bad Adress"),
        ("DAMAGED", "Damaged Product"),
        ("REFUSED", "Customer Refused"),
    )
    exception_type = models.CharField(max_length=50, choices=exception_choices)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    notes = models.TextField()