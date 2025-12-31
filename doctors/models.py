from django.db import models
from accounts.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    fees = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Availability(models.Model):
    DAYS = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="availabilities"
    )
    day = models.CharField(max_length=20, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ["day", "start_time"] 

    def __str__(self):
        return f"{self.doctor.user.username} - {self.day} ({self.start_time}-{self.end_time})"


class Medicine(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="medicines"
    )
    name = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)  

    class Meta:
        ordering = ["name"]  

    def __str__(self):
        return f"{self.name} - {self.doctor.user.username}"
