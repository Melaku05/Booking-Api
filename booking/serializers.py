from email.policy import default
from .models import Doctor, Reservation
from rest_framework import serializers
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'detail', 'photo',  'city', 'specialization', 'fee',  'created_at', 'updated_at']

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Reservation
        fields = ['id', 'city', 'date', 'doctor','user', 'created_at', 'updated_at']

