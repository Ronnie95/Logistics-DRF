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

class HOSLog(models.Model):
    hos_choices = (
        ("OFF", "off"),
        ("ON", "on"),
        ("DRIVING", "driving"),
        ("SLEPPER BERTH", "sb")
    )
    hos_type = models.CharField(max_length=50, choices=hos_choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #driver permissions will be updated 


class PreTripInspection(models.Model):

    trucks = models.ForeignKey(
        Truck,
        on_delete=models.CASCADE,
        related_name="inspections"
    )

    # driver = models.ForeignKey(
    #     Driver,
    #     on_delete=models.CASCADE
    # )

    completed_at = models.DateTimeField(
        auto_now_add=True
    )

    overall_passed = models.BooleanField(
        default=True
    )

class InspectionItem(models.Model):

    inspection = models.ForeignKey(
        PreTripInspection,
        on_delete=models.CASCADE,
        related_name="items"
    )

    item_name = models.CharField(
        max_length=100
    )

    passed = models.BooleanField()

    notes = models.TextField(
        blank=True
    )

class MaintenanceRecord(models.Model):

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETE", "Complete"),
    ]

    trucks = models.ForeignKey(
        Truck,
        on_delete=models.CASCADE,
        related_name="maintenance_records"
    )

    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    opened_date = models.DateTimeField(
        auto_now_add=True
    )

    completed_date = models.DateTimeField(
        null=True,
        blank=True
    )

class MaintenanceItem(models.Model):

    maintenance_record = models.ForeignKey(
        MaintenanceRecord,
        on_delete=models.CASCADE,
        related_name="items"
    )

    description = models.CharField(
        max_length=255
    )

    labor_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    completed = models.BooleanField(
        default=False
    )