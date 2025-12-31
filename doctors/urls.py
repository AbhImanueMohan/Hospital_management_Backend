from django.urls import path
from .views import (
    DoctorProfileView,
    DoctorListView,
    DoctorDetailView,
    DoctorSearchView,
    AvailabilityListCreateView,
    AvailabilityDeleteView,
    MedicineListCreateView,
    MedicineDeleteView,
    DoctorAppointmentsView, 
)

urlpatterns = [

    path("profile/", DoctorProfileView.as_view(), name="doctor-profile"),
    path("", DoctorListView.as_view(), name="doctor-list"),
    path("search/", DoctorSearchView.as_view(), name="doctor-search"),
    path("<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
    path("availabilities/", AvailabilityListCreateView.as_view(), name="availability-list-create"),
    path("availabilities/<int:pk>/", AvailabilityDeleteView.as_view(), name="availability-delete"),
    path("medicines/", MedicineListCreateView.as_view(), name="medicine-list-create"),
    path("medicines/<int:pk>/", MedicineDeleteView.as_view(), name="medicine-delete"),
    path("appointments/", DoctorAppointmentsView.as_view(), name="doctor-appointments"),  # NEW
]
