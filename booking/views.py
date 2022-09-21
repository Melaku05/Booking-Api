from rest_framework.viewsets import ModelViewSet 
from rest_framework import permissions
from .models import Doctor, Reservation
from .serializers import DoctorSerializer, ReservationSerializer
# Create your views here.

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
             return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]


class ReservationViewSet(ModelViewSet):
    queryset =Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Reservation.objects.all()
        
        return Reservation.objects.filter(user=user)
        
