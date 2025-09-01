from django.db import models
from clientes.models import Cliente
from loan.models import Ahorro, Pago

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ("DEPOSITO", "Depósito"),
        ("RETIRO", "Retiro"),
        ("PAGO", "Pago"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="transacciones")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    # Opcional, solo uno se usará por transacción
    ahorro = models.ForeignKey(Ahorro, on_delete=models.CASCADE, null=True, blank=True, related_name="transacciones")
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null=True, blank=True, related_name="transacciones")

    def save(self, *args, **kwargs):
        # Si es depósito o retiro, actualizar total del ahorro
        if self.ahorro:
            if self.tipo == "DEPOSITO":
                self.ahorro.monto_inicial += self.monto
            elif self.tipo == "RETIRO":
                self.ahorro.monto_inicial -= self.monto
            self.ahorro.save()

        # Si es pago de crédito, actualizar saldo_restante
        if self.pago and self.tipo == "PAGO":
            total_pagado = Pago.objects.filter(credito=self.pago.credito).exclude(pk=self.pago.pk).aggregate(
                total=models.Sum('pago')
            )['total'] or 0
            self.pago.saldo_restante = self.pago.credito.monto_inicial - (total_pagado + self.pago.pago)
            self.pago.save()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"

    def __str__(self):
        destino = self.ahorro or self.pago
        return f"{self.tipo} de Q{self.monto} - {destino} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
