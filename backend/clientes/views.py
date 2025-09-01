from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClienteSerializer, ContactoSerializer, DocumentsSerliarizer
from .models import Cliente, Contacto, Documents

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
    