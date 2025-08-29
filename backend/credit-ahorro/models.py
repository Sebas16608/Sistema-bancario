from django.db import models
from clientes.models import Cliente
# Create your models here.

class Credito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"Crédito de {self.cliente.full_name} - {self.monto_total}"

class Pago(models.Model):
    credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_restante = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        # Suma todos los pagos anteriores de este crédito
        pagos_anteriores = Pago.objects.filter(credito=self.credito).exclude(id=self.id)
        total_pagado = sum(p.monto_pagado for p in pagos_anteriores) + self.monto_pagado
        
        # Calcula el saldo restante
        self.saldo_restante = max(self.credito.monto_total - total_pagado, 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pago de {self.monto_pagado} - Saldo restante: {self.saldo_restante}"

class Ahorro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        # Suma todos los ahorros anteriores de este cliente
        ahorros_anteriores = Ahorro.objects.filter(cliente=self.cliente).exclude(id=self.id)
        total_ahorrado = sum(a.monto for a in ahorros_anteriores) + self.monto
        
        # Actualiza el saldo total
        self.saldo_total = total_ahorrado
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ahorro de {self.monto} - Saldo total: {self.saldo_total}"