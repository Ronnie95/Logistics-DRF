from django.urls import path, include
from .views import TrailerViewSet, TruckViewSet, DeliveryViewSet, DeliveryExceptionsViewSet, RoutesViewSet, PreTripInspectionViewSet, CustomerInfoViewSet, MaintenanceItemViewSet, MaintenanceRecordViewSet, HOSLogViewSet, InspectionItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trailers', TrailerViewSet)
router.register(r'trucks', TruckViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'deliveryexceptions', DeliveryExceptionsViewSet)
router.register(r'routes', RoutesViewSet)
router.register(r'pretrip', PreTripInspectionViewSet)
router.register(r'customers', CustomerInfoViewSet)
router.register(r'maintenanceitems', MaintenanceItemViewSet)
router.register(r'maintenancerecors', MaintenanceRecordViewSet)
router.register(r'hos', HOSLogViewSet)
router.register(r'inspectionitems', InspectionItemViewSet)
