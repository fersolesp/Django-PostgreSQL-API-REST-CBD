from rest_framework import serializers

from .models import *

class marcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class combustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combustible
        fields = '__all__'

class cajaCambiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CajaCambios
        fields = '__all__'

class traccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traccion
        fields = '__all__'

class modeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class articuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class tipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'

class versionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'