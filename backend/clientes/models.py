from django.db import models

# Create your models here.
# CLiente
class Cliente(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dpi = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.full_name
