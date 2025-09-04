from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    ROLES = [
        ("JEFE", "Jefe"),
        ("CAJERO", "Cajero"),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default="CAJERO")  # ojo que default sea consistente

    