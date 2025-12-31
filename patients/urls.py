from django.urls import path
from .views import PatientProfileView

urlpatterns = [
    path('dashboard/', PatientProfileView.as_view(), name='patient-dashboard'),
]
