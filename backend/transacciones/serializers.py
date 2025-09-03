from .models import Transaccion
from rest_framework import serializers

class TransaccionSerializer(serializers.ModelSerializer):
    model = Transaccion
    fields = "__all__"