from django.urls import path, include
from .views import TrailerViewSet, TruckViewSet, DeliveryViewSet, DeliveryExceptionsViewSet, RoutesViewSet, PreTripInspectionViewSet, CustomerInfoViewSet, MaintenanceItemViewSet, MaintenanceRecordViewSet, HOSLogViewSet, InspectionItemViewSet, RegisterView
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


urlpatterns = [

    path('',include(router.urls)),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
]