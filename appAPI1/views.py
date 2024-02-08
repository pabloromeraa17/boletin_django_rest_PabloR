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

    @action(detail=False, methods=['GET'])
    def vehiculos_por_marca(self, request):
        nombre_marca = request.query_params.get('nombre', None)

        try:
            marca = Marca.objects.get(nombre=nombre_marca)
            vehiculos = Vehiculo.objects.filter(marca=marca)
            serializer = VehiculoSerializer(vehiculos, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'La marca no existe'})

    @action(detail=False, methods=['GET'])
    def vehiculos_por_fecha(self, request):
        vehiculos = Vehiculo.objects.all().order_by('fecha_matriculacion')
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def filtrar_vehiculos(self, request):
        marca = request.query_params.get('marca', None)
        modelo = request.query_params.get('modelo', None)
        color = request.query_params.get('color', None)

        kwargs = {}
        if marca:
            kwargs['marca__nombre'] = marca
        if modelo:
            kwargs['modelo__icontains'] = modelo
        if color:
            kwargs['color'] = color

        vehiculos = Vehiculo.objects.filter(**kwargs)
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)