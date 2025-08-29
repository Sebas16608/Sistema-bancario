from django.db import models

# Create your models here.
# CLiente
class Cliente(models.Model):
    full_name = models.CharField(max_length=255)
    dpi = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField(upload_to="media")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.full_name} - {self.dpi}"
# Contacto
class Contacto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="contactos")
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.TextField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.cliente.full_name} - {self.telefono}"
     