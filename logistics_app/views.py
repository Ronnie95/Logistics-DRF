from django.shortcuts import render
from .models import Trailer, Truck, Routes, CustomerInfo, DeliverExceptions, Delivery, HOSLog, PreTripInspection, InspectionItem, MaintenanceItem, MaintenanceRecord
from rest_framework.viewsets import ModelViewSet
from .serializers import MaintenanceRecordSerializer, MaintenanceItemSerializer, InspectionItemSerializer, PreTripSerializer, HOSLogSerializer, DeliverExceptionSerializer, CustomerInfoSerializer, TrailerSerializer, TruckSerializer, DeliverySerializer, RoutesSerializer
# Create your views here.

