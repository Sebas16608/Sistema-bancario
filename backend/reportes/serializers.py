from clientes.models import Cliente, Documents, Contacto
from loan.models import Credito, Pago, Ahorro, Deposito
from transacciones.models import Transaccion
from user.models import User
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "full_name", "nacionalidad"]

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ["telefono", "email", "direccion"]

class DocummentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ["identificacion", "no_identificacion", "vivienda"]


class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = ["monto_inicial", "plazo", "interes"]

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ["fecha", "pago", "saldo_restante"]

class AhorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ahorro
        fields = ["tipo", "fecha", "monto_inicial"]

class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ["fecha", "monton"]

class TransaccionSerializer(serializers.ModelSerializer):
    class meta:
        model = Transaccion
        field = ["tipo", "monto", "fecha", "ahorro", "credito"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "rol"]
