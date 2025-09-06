from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    full_name = models.CharField(max_length=100)

    ROLES = [
        ("JEFE", "Jefe"),
        ("CAJERO", "Cajero"),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default="CAJERO")

    # Evitar conflictos con auth.User
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


    def __str__(self):
        return self.username
