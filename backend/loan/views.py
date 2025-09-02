from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CreditoSerializer, PagoSerializer, AhorroSerializer, DepositoSerializer
from .models import Credito, Pago, Ahorro, Deposito

"""
API  Credito
"""
class CreditoView(APIView):
    # Metodo GET
    def get(self, request, pk=None):
        if pk:
            try:
                credito = Credito.objects.get(pk=pk)
                serializer = CreditoSerializer(credito)
                return Response(serializer.data)
            except Credito.DoesNotExist:
                return Response({"error": "Credito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            credito = Credito.objects.all()
            serializer = CreditoSerializer(credito, many=True)
            return Response(serializer.data)
        
    # Metodo POST
    def post(self, request):
        serilizer = CreditoSerializer
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo PUT
    def put(self, request, pk):
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response({"error": "El credito  no fue encontradro"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CreditoSerializer(credito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo DELETE
    def delete(self, request, pk):
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response({"error": "Credito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        credito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)