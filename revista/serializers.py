from rest_framework import serializers
from .models import Categorias,Revista, Subcategorias
from planrevista.models import PlanRevista
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer, NomCiudadSerializer

class NomPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   ['nombre']

class RevistaPlanSerializer(serializers.ModelSerializer):
    plan    =   NomPlanSerializer(many=False, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista','plan']

class RevistaSerializer(serializers.ModelSerializer):
    plan    =   NomPlanSerializer(many=False, read_only=True)
    country =   NomRegionSerializer(many=False, read_only=True)
    state   =   NomSubregionSerializer(many=False, read_only=True)
    city    =   NomCiudadSerializer(many=False, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   '__all__'

class NomRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']

class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   NomRevistaSerializer(read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

class NomCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Categorias
        fields  =   ['nombre_categoria']

class NomSubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subcategorias
        fields  =   ['nombre_subcategoria']