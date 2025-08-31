from django.contrib import admin
from .models import Credito, Pago, Ahorro, Deposito
# Register your models here.
admin.site.register(Credito)
admin.site.register(Pago)
admin.site.register(Ahorro)
admin.site.register(Deposito)
