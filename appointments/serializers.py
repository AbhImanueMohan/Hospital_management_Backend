from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'time', 'status']
        read_only_fields = ['id', 'patient', 'status']  # patient and status will be added automatically
