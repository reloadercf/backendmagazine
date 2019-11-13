from rest_framework import serializers
from .models import Region,Subregion, Ciudad

#serializador para sacar nombre de pais
class NomRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Region
        fields  =   ['nombre_pais']

#serializador para sacar nombre de estado
class NomSubregionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subregion
        fields  =   ['nombre_estado']

#serializador para sacar nombre de ciudad
class NomCiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Ciudad
        fields  =   ['nombre_ciudad']

#serializador para CRUD de pais
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Region
        fields  =   '__all__'

#serializador para datos de estado
class SubregionSerializer(serializers.ModelSerializer):
    pais        =   NomRegionSerializer(many = True, read_only=True)
    class Meta:
        model   =   Subregion
        fields  =   '__all__'

#serializador para CRUD de estado
class POSTSubegionSerializer(serializers.ModelSerializer):
    pais        =   serializers.PrimaryKeyRelatedField(
                    queryset=Region.objects.all(),
                    required=True,
                    many= True)
    class Meta:
        model   =   Subregion
        fields  =   '__all__'

#serializador para datos de ciudad
class CiudadSerializer(serializers.ModelSerializer):
    estado      =   NomSubregionSerializer(many= True, read_only=True)
    class Meta:
        model   =   Ciudad
        fields  =   '__all__'

#serializador para CRUD de ciudad
class POSTCiudadSerializer(serializers.ModelSerializer):
    estado      =   serializers.PrimaryKeyRelatedField(
                    queryset=Subregion.objects.all(),
                    required=True,
                    many= True)
    class Meta:
        model   =   Ciudad
        fields  =   '__all__'