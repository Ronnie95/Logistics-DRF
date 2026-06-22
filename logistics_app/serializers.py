from .models import Routes, Delivery
from rest_framework import serializers, 
from rest_framework.serializers import ModelSerializer



class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('id','stop','customer_name', 'delivery_window', 'pickup_location', 'dropoff_location', 'order_number', 'status') 



class RoutesSerializer(ModelSerializer):
    class Meta:
        model = Routes
        fields = ('id','route_name','deliveries') 
