from rest_framework import serializers
from .models import Doctor, Availability, Medicine
from accounts.models import User


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ["id", "day", "start_time", "end_time"]


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ["id", "name", "fee", "description"]


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class DoctorSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)
    availabilities = AvailabilitySerializer(many=True, read_only=True)
    medicines = MedicineSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = [
            "id",
            "user",
            "specialization",
            "department",
            "qualification",
            "experience",
            "fees",
            "is_active",
            "availabilities",
            "medicines",
        ]
        read_only_fields = ["id", "user", "is_active"]
