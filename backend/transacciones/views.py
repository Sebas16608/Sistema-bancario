from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransaccionSerializer
from .models import Transaccion
# Create your views here.
class TransaccionView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                transacciones = Transaccion.objects.get(pk=pk)
                serializer = TransaccionSerializer(transacciones, many=True)
                return Response(serializer.data)
            except Transaccion.DoesNotExist:
                return Response({"error": "Transaccion no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        else:
            transacciones = Transaccion.objects.all()
            serializer = TransaccionSerializer(transacciones, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = TransaccionSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            transacciones = Transaccion.objects.get(pk)
        except Transaccion.DoesNotExist:
            return Response({"error": "Transaccion no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransaccionSerializer(transacciones, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            trasaccion = Transaccion.objects.get(pk)
        except Transaccion.DoesNotExist:
            return Response({"error": "Transaccion no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        trasaccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
