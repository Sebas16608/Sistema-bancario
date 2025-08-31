from django.db import models
from clientes.models import Cliente
# Create your models here.

#Credito 
class Credito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="credito")
    monto = models.CharField(max_length=10)
    plazo = models.CharField(max_length=10)

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("APROBADO", "Aprobado"),
        ("RECHAZADO", "Rechazado")
    ]

class Pago(models.Model):
    credito = models.ForeignKey(Credito, on_delete=models.CASCADE, related_name="pago")
    fecha = models.DateField()
    pago = models.CharField(max_length=255)
    saldo_restante = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        # Calculamos el saldo restante antes de guardar
        total_pagado = Pago.objects.filter(credito=self.credito).exclude(pk=self.pk).aggregate(
            total=models.Sum('pago')
        )['total'] or 0

        self.saldo_restante = self.credito.monto_inicial - (total_pagado + self.pago)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"Pago de {self.pago} el {self.fecha} - Saldo restante: {self.saldo_restante}"