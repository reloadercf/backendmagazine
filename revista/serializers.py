from rest_framework import serializers
from .models import Categorias,Revista, Subcategorias
from planrevista.models import PlanRevista
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer, NomCiudadSerializer
from regiones.models import *
from accounts.models import Profile

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

class POSTRevistaSerializer(serializers.ModelSerializer):
    plan    =   serializers.PrimaryKeyRelatedField(
                        queryset=PlanRevista.objects.all(),
                        required=False,
                        many=False)
    country =   serializers.PrimaryKeyRelatedField(
                        queryset=Region.objects.all(),
                        required=False,
                        many=False)
    state   =   serializers.PrimaryKeyRelatedField(
                        queryset=Subregion.objects.all(),
                        required=False,
                        many=False)
    city    =   serializers.PrimaryKeyRelatedField(
                        queryset=Ciudad.objects.all(),
                        required=False,
                        many=False)
    class Meta:
        model   =   Revista
        fields  =   ['id','nombre_revista', 'plan', 'country', 'state', 'city']
    

# class AddRevistaProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model   =  Profile
#         fields  =   ['id', 'revista']


class NomRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']

class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   NomRevistaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

class POSTCategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   serializers.PrimaryKeyRelatedField(
                        queryset=Revista.objects.all(),
                        required=True,
                        many=False)
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

class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   NomCategoriaSerializer(many=False, read_only=True)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'

class POSTSubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   serializers.PrimaryKeyRelatedField(
                        queryset=Categorias.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'