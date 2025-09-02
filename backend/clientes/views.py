from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClienteSerializer, ContactoSerializer, DocumentsSerliarizer
from .models import Cliente, Contacto, Documents
"""
API Clientes
"""
class ClienteView(APIView):
    # Metodo Get
    def get(self, request, pk=None):
        if pk:
            try:
                cliente = Cliente.objects.get(pk=pk)
                serializer = ClienteSerializer(cliente)
                return Response(serializer.data)
            except Cliente.DoesNotExist:
                return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            cliente = Cliente.objects.all()
            serializer = ClienteSerializer(cliente, many=True)
            return Response(serializer.data)
    
    # Metodo POST
    def post(self, request):
        serializer = ClienteSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo PUT
    def put(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo DELETE
    def delete(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
API Contacto
"""
class ContactoView(APIView):
    # Metodo GET
    def get(self, request, pk=None):
        if pk:
            try:
                contacto = Contacto.objects.get(pk=pk)
                serializer = ContactoSerializer(contacto,)
                return Response(serializer.data)
            except Contacto.DoesNotExist:
                return Response({"error": "Contacto no no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            contacto = Contacto.objects.all()
            serializer = ContactoSerializer(contacto, many=True)
            return Response(serializer.data)

    # Metodo POST
    def post(self, request):
        serializer = ContactoSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
