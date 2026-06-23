from .models import Routes, Delivery, Trailer, Truck, CustomerInfo, DeliverExceptions, HOSLog, PreTripInspection, InspectionItem, MaintenanceRecord

from rest_framework import serializers, 
from rest_framework.serializers import ModelSerializer

class TruckSerializer(ModelSerializer):
    model = Truck 
    fields = ('truck_number', 'make', 'model', 'year', 'truck_options')

class TrailerSerializer(ModelSerializer):
    model = Trailer 
    fields = ('trailer_number', 'trailer_option')
    class Meta:
        model = Delivery
        fields = ('id','stop','customer_name', 'delivery_window', 'pickup_location', 'dropoff_location', 'order_number', 'status') 


class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields = ('id','route_name','route_date', 'trucks', 'trailers') 


class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields = ('id','route_name','route_date', 'trucks', 'trailers') 

class CustomerInfoSerializer(ModelSerializer):
    class Meta:
        model = CustomerInfo 
        fields = ('id', 'name', 'address', 'city', 'state')


class DeliverySerializer(ModelSerializer):
    class meta:
        model: Delivery
        fields = ('id', 'routes', 'customer', 'order_number', 'status', 'delivered_at')


class DeliverExceptionSerializer(ModelSerializer):
    class Meta:
        model =  DeliverExceptions
        fields = ("id", 'exception_type', 'delivery', 'notes')

class HOSLogSerializer(ModelSerializer):
    class Meta:
        model = HOSLog 
        fields = ('id','hos_type', 'start_time', 'end_time')
    
class PreTripSerializer(ModelSerializer):
    class Meta:
        model = PreTripInspection
        fields = ('id', 'trucks', 'completed_at', 'overall_passed')
    
class InspectionItemSerializer(ModelSerializer):
    class Meta:
        model = InspectionItem 
        fields = ('id', 'inspection', 'item_name', 'passed', 'notes')

class MaintenanceRecordSerializer(ModelSerializer):
    class Meta:
        model = MaintenanceRecord 
        fields = ('id', 'trucks', 'status','opened_date', 'completed_date')

class MaintenanceItemSerializer(ModelSerializer):
    class Meta:
        model = MaintenanceItem 
        fields = ('id', 'maintenance_record', 'description','labor_hours', 'completed')
