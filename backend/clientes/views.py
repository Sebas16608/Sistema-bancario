from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClienteSerializer, ContactoSerializer, DocumentsSerliarizer
from .models import Cliente, Contacto, Documents
# Create your views here.
class Cliente(APIView):
    def get(self, request):
        cliente = Contacto.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    
        