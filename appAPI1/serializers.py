from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Marca, Vehiculo

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombre']

class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['tipo_vehiculo', 'chasis', 'marca', 'modelo', 'matricula', 'color', 'fecha_fabricacion', 'fecha_matriculacion', 'fecha_baja', 'suspendido']