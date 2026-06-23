from .models import Routes, Delivery, Trailer, Truck
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
