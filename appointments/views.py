from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from patients.models import Patient

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        patient = Patient.objects.get(user=self.request.user)
        serializer.save(patient=patient)
