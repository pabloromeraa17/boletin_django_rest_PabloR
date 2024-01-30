from django.shortcuts import render
from rest_framework import viewsets
from .models import Marca, Vehiculo
from .serializers import MarcaSerializer, VehiculoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    @action(detail=True, methods=['GET'])
    def vehiculos_por_marca(self, request, pk=None):
        marca = Marca.objects.get(pk=pk)
        vehiculos = Vehiculo.objects.filter(marca=marca)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)