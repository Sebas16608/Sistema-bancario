from .serializers import ClienteSerializer, DocummentSerializer, ContactoSerializer, CreditoSerializer, PagoSerializer, AhorroSerializer, DepositoSerializer, UserSerializer, TransaccionSerializer
from clientes.models import Cliente, Documents, Contacto
from loan.models import Credito, Pago, Ahorro, Deposito
from transacciones.models import Transaccion
from user.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ClienteView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                clientes = Cliente.objects.get(pk=pk)
                serializer = ClienteSerializer(clientes)
                return Response(serializer.data)
            except Cliente.DoesNotExist:
                return Response({"error": "el cliente no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data)
        
class ContactoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                contactos = Contacto.objects.get(pk=pk)
                serializer = ContactoSerializer(contactos)
                return Response(serializer.data)
            except Contacto.DoesNotExist:
                return Response({"error": "El contacto no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clientes = Contacto.objects.all()
            serializer = ContactoSerializer(clientes, many=True)
            return Response(serializer.data)
        
class DocView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                documentos = Documents.objects.get(pk=pk)
                serializer = DocummentSerializer(documentos)
                return Response(serializer.data)
            except Documents.DoesNotExist:
                return Response({"error": "Documento no encontrado"})
        else:
            documentos = Documents.objects.all()
            serializer = DocummentSerializer(documentos, many=True)

class CreditoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                creditos = Credito.objects.get(pk=pk)
                serializer = CreditoSerializer(creditos)
                return Response(serializer.data)
            except Credito.DoesNotExist:
                return Response({"error", "El credito no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            creditos = Credito.objects.all()
            serializer = CreditoSerializer(creditos, many=True)
            return Response(serializer.data)
        
class PagoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                pagos = Pago.objects.get(pk=pk)
                serializer = PagoSerializer(pagos)
                return Response(serializer.data)
            except Pago.DoesNotExist:
                return Response({"error":"El pago no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            pagos = Pago.objects.all()
            serializer = PagoSerializer(pagos, many=True)
            return Response(serializer.data)

class AhorroView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                ahorros = Ahorro.objects.get(pk=pk)
                serializer = AhorroSerializer(ahorros)
                return Response(serializer.data)
            except Ahorro.DoesNotExist:
                return Response({"error": "El ahorro no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            ahorros = Ahorro.objects.all()
            serializer = AhorroSerializer(ahorros, many=True)
            return Response(serializer.data)
        
class DepositoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                depositos = Deposito.objects.get(pk=pk)
                serilizer = DepositoSerializer(depositos)
                return Response(serilizer.data)
            except Deposito.DoesNotExist:
                return Response({"error": "El deposito no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            depositos = Deposito.objects.all()
            serilizer = DepositoSerializer(depositos, many=True)
            return Response(serilizer.data)
        
class UserView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                users = User.objects.get(pk=pk)
                serializer = UserSerializer(users)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        
class TrasaccionView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                transacciones = Transaccion.objects.get(pk=pk)
                serializer = TransaccionSerializer(transacciones)
                return Response(serializer.data)
            except Transaccion.DoesNotExist:
                return Response({"error": "Transaccion no encontrada"}, status=status.HTTP_404_NOT_FOUND)