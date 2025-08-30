from django.contrib import admin
from clientes.models import Cliente, Contacto, Documents
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Documents)
