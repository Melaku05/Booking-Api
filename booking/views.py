from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Doctor, Reservation
from .serializers import DoctorSerializer, ReservationSerializer
# Create your views here.
class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer