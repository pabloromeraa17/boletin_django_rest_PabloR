from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, permissions, filters
from .models import Marca, Vehiculo
from .serializers import MarcaSerializer, VehiculoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    # @action(detail=True, methods=['GET'])
    # def listadoVehiculos(self, request, pk):
    #     marca = get_object_or_404(Marca, pk=pk)
    #     vehiculos = Vehiculo.objects.filter(marca=marca)
    #     serializer = VehiculoSerializer(vehiculos, many=True, context={'request': request})
    #     return Response(serializer.data)

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['marca']
    ordering_fields = ['fecha_fabricacion']

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(name='marca', description="", required=False, type=str)
    #     ]
    # )
    # @action(detail=False, methods=['GET'], description="Filter on marca get parameter")
    # def filtro_marca(self, request):
    #     vehiculos_marca = Vehiculo.objects.all()
    #     marca = self.request.query_params.get('marca')
    #     if marca:
    #         vehiculos_marca = vehiculos_marca.filter(marca__nombre=marca)
    #
    #     serializer = self.get_serializer(vehiculos_marca, many=True)
    #     return Response(serializer.data)

    # @action(detail=False, methods=['GET'])
    # def vehiculos_por_marca(self, request):
    #     nombre_marca = request.query_params.get('nombre', None)
    #
    #     try:
    #         marca = Marca.objects.get(nombre=nombre_marca)
    #         vehiculos = Vehiculo.objects.filter(marca=marca)
    #         serializer = VehiculoSerializer(vehiculos, many=True)
    #         return Response(serializer.data)
    #     except ObjectDoesNotExist:
    #         return Response({'error': 'La marca no existe'})

    # @action(detail=False, methods=['GET'])
    # def vehiculos_por_fecha(self, request):
    #     vehiculos = Vehiculo.objects.all().order_by('fecha_matriculacion')
    #     serializer = VehiculoSerializer(vehiculos, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['GET'])
    # def filtrar_vehiculos(self, request):
    #     marca = request.query_params.get('marca', None)
    #     modelo = request.query_params.get('modelo', None)
    #     color = request.query_params.get('color', None)
    #
    #     kwargs = {}
    #     if marca:
    #         kwargs['marca__nombre'] = marca
    #     if modelo:
    #         kwargs['modelo__icontains'] = modelo
    #     if color:
    #         kwargs['color'] = color
    #
    #     vehiculos = Vehiculo.objects.filter(**kwargs)
    #     serializer = VehiculoSerializer(vehiculos, many=True)
    #     return Response(serializer.data)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]