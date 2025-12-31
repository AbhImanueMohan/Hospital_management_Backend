from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "Hospital Management API is running"})

urlpatterns = [
    path("", home),  # health check
    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/patient/", include("patients.urls")),
    path("api/appointments/", include("appointments.urls")),
]
