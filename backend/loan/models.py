from django.db import models
from clientes.models import Cliente

# Credito 
class Credito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="creditos")
    monto_inicial = models.DecimalField(max_digits=12, decimal_places=2)
    plazo = models.CharField(max_length=10)
    interes = models.CharField(max_length=10)

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("APROBADO", "Aprobado"),
        ("RECHAZADO", "Rechazado"),
    ]

    def __str__(self):
        return f"Crédito de {self.monto_inicial} - {self.cliente}"


# Pago
class Pago(models.Model):
    credito = models.ForeignKey(Credito, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    pago = models.DecimalField(max_digits=12, decimal_places=2)
    saldo_restante = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
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


# Ahorro
class Ahorro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ahorros")
    tipo = models.CharField(max_length=50)  # Ejemplo: Plazo fijo, ahorro mujer, etc.
    fecha = models.DateField()
    monto_inicial = models.DecimalField(max_digits=12, decimal_places=2)
    
    def total_ahorrado(self):
        deposito = self.depositos.aggregate(total=models.Sum("monto"))["total"] or 0
        return self.monto_inicial + deposito

    class Meta:
        verbose_name = "Ahorro"
        verbose_name_plural = "Ahorros"

    def __str__(self):
        return f"{self.cliente} - {self.tipo} - Total: {self.total_ahorrado()}"


# Deposito
class Deposito(models.Model):
    ahorro = models.ForeignKey(Ahorro, on_delete=models.CASCADE, related_name="depositos")
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Depósito de {self.monto} el {self.fecha}"
