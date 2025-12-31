from rest_framework import serializers
from .models import Patient
from accounts.models import User


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class PatientSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id",
            "user",
            "age",
            "disease",
            "medicines",
            "tests_done",
            "next_visit",
        ]
