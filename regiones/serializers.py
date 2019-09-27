from rest_framework import serializers
from .models import Region,Subregion, Ciudad

class NomRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Region
        fields  =   ['nombre_pais']

class NomSubregionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subregion
        fields  =   ['nombre_estado']

class NomCiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Ciudad
        fields  =   ['nombre_ciudad']