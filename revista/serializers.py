from rest_framework import serializers
from .models import Categorias,Revista, Subcategorias
from planrevista.models import PlanRevista
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer, NomCiudadSerializer
from regiones.models import *
from accounts.models import Profile

#serializador para sacar nombre de plan de la revista
class NomPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   ['nombre']

#serializador para sacar nombre de plan y de la revista
class RevistaPlanSerializer(serializers.ModelSerializer):
    plan    =   NomPlanSerializer(many=False, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista','plan']

#serializador para sacar datos de la revista
class RevistaSerializer(serializers.ModelSerializer):
    plan    =   NomPlanSerializer(many=False, read_only=True)
    country =   NomRegionSerializer(many=False, read_only=True)
    state   =   NomSubregionSerializer(many=False, read_only=True)
    city    =   NomCiudadSerializer(many=False, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   '__all__'

#serializador CRUD de revista
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

#serializador para sacar nombre de la revista
class NomRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']

#serializador para sacar datos de la categoria
class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   NomRevistaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

#serializador para CRUD de categoria
class POSTCategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   serializers.PrimaryKeyRelatedField(
                        queryset=Revista.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

#serializador para sacar nombre de categoria
class NomCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Categorias
        fields  =   ['nombre_categoria']

#serializador para sacar nombre de subcategoria
class NomSubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subcategorias
        fields  =   ['nombre_subcategoria']

#serializador para datos de subcategoria
class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   NomCategoriaSerializer(many=False, read_only=True)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'

#serializador para CRUD de subcategoria
class POSTSubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   serializers.PrimaryKeyRelatedField(
                        queryset=Categorias.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'