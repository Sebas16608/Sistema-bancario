from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CreditoSerializer, PagoSerializer, AhorroSerializer, DepositoSerializer
from .models import Credito, Pago, Ahorro, Deposito

"""
API Credito
"""
class CreditoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                credito = Credito.objects.get(pk=pk)
                serializer = CreditoSerializer(credito)
                return Response(serializer.data)
            except Credito.DoesNotExist:
                return Response({"error": "Credito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            creditos = Credito.objects.all()
            serializer = CreditoSerializer(creditos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CreditoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response({"error": "Credito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CreditoSerializer(credito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response({"error": "Credito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        credito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
API Pago
"""
class PagoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                pago = Pago.objects.get(pk=pk)
                serializer = PagoSerializer(pago)
                return Response(serializer.data)
            except Pago.DoesNotExist:
                return Response({"error": "Pago no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            pagos = Pago.objects.all()
            serializer = PagoSerializer(pagos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            pago = Pago.objects.get(pk=pk)
        except Pago.DoesNotExist:
            return Response({"error": "Pago no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PagoSerializer(pago, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            pago = Pago.objects.get(pk=pk)
        except Pago.DoesNotExist:
            return Response({"error": "Pago no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        pago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
API Ahorro
"""
class AhorroView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                ahorro = Ahorro.objects.get(pk=pk)
                serializer = AhorroSerializer(ahorro)
                return Response(serializer.data)
            except Ahorro.DoesNotExist:
                return Response({"error": "Ahorro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            ahorros = Ahorro.objects.all()
            serializer = AhorroSerializer(ahorros, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AhorroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            ahorro = Ahorro.objects.get(pk=pk)
        except Ahorro.DoesNotExist:
            return Response({"error": "Ahorro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AhorroSerializer(ahorro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            ahorro = Ahorro.objects.get(pk=pk)
        except Ahorro.DoesNotExist:
            return Response({"error": "Ahorro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        ahorro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
API Deposito
"""
class DepositoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                deposito = Deposito.objects.get(pk=pk)
                serializer = DepositoSerializer(deposito)
                return Response(serializer.data)
            except Deposito.DoesNotExist:
                return Response({"error": "Deposito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            depositos = Deposito.objects.all()
            serializer = DepositoSerializer(depositos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = DepositoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            deposito = Deposito.objects.get(pk=pk)
        except Deposito.DoesNotExist:
            return Response({"error": "Deposito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepositoSerializer(deposito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            deposito = Deposito.objects.get(pk=pk)
        except Deposito.DoesNotExist:
            return Response({"error": "Deposito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        deposito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
API Ahorro
"""
class AhorroView(APIView):
    # Metodo GET
    def get(self, request, pk=None):
        if pk:
            try:
                ahorro = Ahorro.objects.get(pk=pk)
                serializer = AhorroSerializer(ahorro, many=True)
                return Response(serializer.data)
            except Ahorro.DoesNotExist:
                return Response({"error": "El ahorro no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            ahorro = Ahorro.objects.all()
            serializer = AhorroSerializer(ahorro, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        try:
            serializer = AhorroSerializer
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Ahorro.DoesNotExist:
            return Response({"error": "El ahorro no fue encontro"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            ahorro = Ahorro.objects.get(pk=pk)
        except Ahorro.DoesNotExist:
            return Response({"error": "El ahorro no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AhorroSerializer(ahorro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            ahorro = Ahorro.objects.get(pk=pk)
        except Ahorro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        ahorro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)