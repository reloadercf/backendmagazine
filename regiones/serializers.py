from rest_framework import serializers
from .models import Region,Subregion

class NomRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Region
        fields  =   ['nombre_pais']

class NomSubregionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subregion
        fields  =   ['nombre_estado']