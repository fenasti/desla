from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class ReservationRequest(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reserver")
    email = models.EmailField()
    details = models.TextField()
    reservation_date = models.DateField(default=timezone.now)  # Separate date field
    reservation_time = models.TimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return (
            f"Reservation request from {self.client.email} for the "
            f"{self.reservation_date} at {self.reservation_time}"
        )