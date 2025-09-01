from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    ROLES = [
        ("ADMINISTRADOR", "Administrador")
        ("CAJERO", "Cajero")
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default="Cajero")
