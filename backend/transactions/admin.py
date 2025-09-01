from django.contrib import admin
from transactions.models import Cuenta, Movimiento
# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Movimiento)
