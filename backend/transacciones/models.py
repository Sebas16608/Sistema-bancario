from django.db import models
from clientes.models import Cliente
# Create your models here.
class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    def __str__(self):
        return f"El pago de {self.pago} fue exitoso en la cuenta de {self.cliente}"
    
class Movimiento(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
    
    def __str__(self):
        return f"movimiento de Q{self.monto} realizado correctamente"