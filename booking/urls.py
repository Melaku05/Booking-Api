from rest_framework import routers
from .views import DoctorViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('reservations', ReservationViewSet, basename='reservation')
urlpatterns = router.urls