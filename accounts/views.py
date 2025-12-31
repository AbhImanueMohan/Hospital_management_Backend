from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, LoginSerializer


# Registration view
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Login view (JWT + role)
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
