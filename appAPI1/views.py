from django.shortcuts import render
from rest_framework import viewsets
from .models import Marca, Vehiculo
from .serializers import MarcaSerializer, VehiculoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def vehiculos_por_marca(self, request, pk=None):
        try:
            marca = Marca.objects.get(nombre=pk)
            vehiculos = Vehiculo.objects.filter(marca=marca)
            serializer = VehiculoSerializer(vehiculos, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'La marca no existe'})