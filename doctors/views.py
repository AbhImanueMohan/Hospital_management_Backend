from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor, Availability, Medicine
from .serializers import (
    DoctorSerializer,
    AvailabilitySerializer,
    MedicineSerializer
)
from .permissions import IsDoctor
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

class DoctorAppointmentsView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    def get_queryset(self):
        return Appointment.objects.filter(doctor__user=self.request.user).order_by("-date", "time")


class DoctorProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    def get(self, request):
        doctor, _ = Doctor.objects.get_or_create(
            user=request.user,
            defaults={
                "specialization": "",
                "qualification": "",
                "experience": 0,
                "fees": 0.0,
            }
        )
        return Response(DoctorSerializer(doctor).data)
    def put(self, request):
        doctor, _ = Doctor.objects.get_or_create(user=request.user)
        serializer = DoctorSerializer(
            doctor, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.select_related("user").all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.select_related("user").all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    def get_object(self):
        doctor = super().get_object()
        if doctor.user != self.request.user:
            self.permission_denied(self.request)
        return doctor

class DoctorSearchView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        department = self.request.query_params.get("department")
        if not department:
            return Doctor.objects.select_related("user").filter(
                department__iexact=department,
                is_active=True
            )

class AvailabilityListCreateView(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    def get_queryset(self):
        return Availability.objects.filter(
            doctor=self.request.user.doctor
        )
    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user.doctor)

class AvailabilityDeleteView(generics.DestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

class MedicineListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    def get_queryset(self):
        return Medicine.objects.filter(
            doctor=self.request.user.doctor
        )
    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user.doctor)

class MedicineDeleteView(generics.DestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
