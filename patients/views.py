from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Patient
from .serializers import PatientSerializer


class PatientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user

        if getattr(user, "role", None) != "patient":
            raise PermissionDenied("Only patients can access this profile.")

        patient, _ = Patient.objects.get_or_create(
            user=user,
            defaults={
                "age": None,
                "disease": "",
                "medicines": "",
                "tests_done": "",
                "next_visit": None,
            }
        )
        return patient
