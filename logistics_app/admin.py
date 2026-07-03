from django.contrib import admin
from .models import Delivery, Routes, Trailer, Truck, PreTripInspection, MaintenanceItem, MaintenanceRecord, CustomerInfo, DeliveryExceptions, HOSLog, InspectionItem
# Register your models here.


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
