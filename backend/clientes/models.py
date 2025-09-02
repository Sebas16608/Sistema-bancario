from django.db import models

# Create your models here.
# CLiente
class Cliente(models.Model):
    full_name = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    
    SI_NO = [
        (True, "Si"),
        (False, "No")
    ]
    extranjero = models.BooleanField(choices=SI_NO, default=False)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.full_name}"
    
# Contacto
class Contacto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="contactos")
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    direccion = models.TextField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.cliente.full_name} - {self.telefono}"

# Documentos     
class Documents(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="documents")

    IDENTIFICACIONES = [
        ("DPI", "DPI"),
        ("PASAPORTE", "Pasaporte"),
        ("LICENCIA", "Licencia"),
        ("CERTIFICADO", "Certificado de Nacimiento")
    ]

    identifiacion = models.CharField(max_length=100, choices=IDENTIFICACIONES)
    no_identificacion = models.CharField(max_length=30)
    
    VIVIENDA = [
        ("PROPIO", "Propio"),
        ("ALQUILADO", "Alquilado"),
        ("PRESTADO", "Prestado")
    ]
    vivienda = models.CharField(choices=VIVIENDA, max_length=20)
    
    RECIBO = [
        ("LUZ", "Luz"),
        ("AGUA", "Agua"),
        ("TELEFONO", "Teléfono")
    ]
    recibo = models.CharField(choices=RECIBO, max_length=20)
    nis = models.CharField(max_length=50)
