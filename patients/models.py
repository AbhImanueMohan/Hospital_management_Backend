from django.db import models
from accounts.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.PositiveIntegerField(null=True, blank=True)
    disease = models.CharField(max_length=200, blank=True)
    medicines = models.TextField(blank=True)

    tests_done = models.TextField(blank=True)   # ✅ ADDED

    next_visit = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
