from .models import Credito, Pago, Ahorro, Deposito
from rest_framework import serializers

class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = "__all__"

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"

class AhorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ahorro
        fields = "__all__"

class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = "__all__"
