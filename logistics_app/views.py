from django.shortcuts import render
from .models import Trailer, Truck, Routes, CustomerInfo, DeliveryExceptions, Delivery, HOSLog, PreTripInspection, InspectionItem, MaintenanceItem, MaintenanceRecord
from rest_framework.viewsets import ModelViewSet
from .serializers import MaintenanceRecordSerializer, MaintenanceItemSerializer, InspectionItemSerializer, PreTripSerializer, HOSLogSerializer, DeliveryExceptionSerializer, CustomerInfoSerializer, TrailerSerializer, TruckSerializer, DeliverySerializer, RoutesSerializer
# Create your views here.

class TruckViewSet(ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class TrailerViewSet(ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

class RoutesViewSet(ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class CustomerInfoViewSet(ModelViewSet):
    queryset =CustomerInfo.objects.all()
    serializer_class =CustomerInfoSerializer

class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer 

class DeliveryExceptionsViewSet(ModelViewSet):
    queryset = DeliveryExceptions.objects.all()
    serializer_class = DeliveryExceptionSerializer

class HOSLogViewSet(ModelViewSet):
    queryset = HOSLog.objects.all()
    serializer_class = HOSLogSerializer

class PreTripInspectionViewSet(ModelViewSet):
    queryset = PreTripInspection.objects.all()
    serializer_class = PreTripSerializer 


class InspectionItemViewSet(ModelViewSet):
    queryset = InspectionItem.objects.all()
    serializer_class = InspectionItemSerializer

class MaintenanceItemViewSet(ModelViewSet):
    queryset = MaintenanceItem.objects.all()
    serializer_class = MaintenanceItemSerializer

class MaintenanceRecordViewSet(ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer 

