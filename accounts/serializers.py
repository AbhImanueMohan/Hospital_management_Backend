from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from patients.models import Patient  


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ("username", "email", "password", "role")

    def create(self, validated_data):
        role = validated_data.get("role")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            role=role,
        )

        if role == "PATIENT":
            Patient.objects.create(user=user)

        return user

class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        token["username"] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["role"] = self.user.role
        data["username"] = self.user.username
        return data
