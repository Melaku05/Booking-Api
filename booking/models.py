from django.db import models
from core.models import User

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    city = models.CharField(max_length=100)
    specialization = models.CharField(max_length=255)
    fee = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    city= models.CharField(max_length=100)
    date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user

