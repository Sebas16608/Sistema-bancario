from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClienteSerializer, ContactoSerializer, DocumentsSerliarizer
from .models import Cliente, Contacto, Documents
# Create your views here.
class ClienteView(APIView):
    # Metodo GET
    def get(self, request):
        cliente = Contacto.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    
    # Metodo POST
    def post(self, request):
        serializer = ClienteSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactoView(APIView):
    # Metodo GET
    def get_contacto(self, request):
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto, many=True)
        return Response(serializer.data)
    
    # Metodo POST
    def post_contact(self, request):
        serializer = ContactoSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)