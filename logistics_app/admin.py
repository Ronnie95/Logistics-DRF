from django.urls import path, include
from django.contrib import admin
from .models import Delivery, Routes, Trailer, Truck, PreTripInspection, MaintenanceItem, MaintenanceRecord, CustomerInfo, DeliveryExceptions, HOSLog, InspectionItem
from rest_framework.routers import DefaultRouter

# Register your models here.

router = DefaultRouter()
admin.site.register(Delivery)
admin.site.register(Routes)
admin.site.register(Trailer)
admin.site.register(Truck)
admin.site.register(PreTripInspection)
admin.site.register(MaintenanceItem)
admin.site.register(MaintenanceRecord)
admin.site.register(CustomerInfo)
admin.site.register(DeliveryExceptions)
admin.site.register(HOSLog)
admin.site.register(InspectionItem)


