from rest_framework import serializers
from .models import Categorias,Revista, Subcategorias
from planrevista.serializers import NomPlanSerializer
from planrevista.models import PlanRevista
from patrocinadores.serializers import DatosPatrocinadorSerializer
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer, NomCiudadSerializer
from articulos.serializers import NomRevistaSerializer, NomCategoriaSerializer, DatosArticuloSerializer
from regiones.models import *
from accounts.models import Profile


#serializador para sacar datos de la revista
class RevistaSerializer(serializers.ModelSerializer):
    # plan        =   NomPlanSerializer(many=False, read_only=True)
    # country     =   NomRegionSerializer(many=True, read_only=True)
    # state       =   NomSubregionSerializer(many=True, read_only=True)
    # city        =   NomCiudadSerializer(many=True, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   ['id', 'nombre_revista', 'logo']

#serializador para sacar datos de la categoria
class CategoriaSerializer(serializers.ModelSerializer):
    #revista_origen  =   NomRevistaSerializer(many=False, read_only=True)
    class Meta:
        model       = Categorias                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        exclude     =['revista_origen']

class RevistaDetalleSerializer(serializers.ModelSerializer):
    plan        =   NomPlanSerializer(many=False, read_only=True)
    country     =   NomRegionSerializer(many=True, read_only=True)
    state       =   NomSubregionSerializer(many=True, read_only=True)
    city        =   NomCiudadSerializer(many=True, read_only=True)
    cat_revista =   CategoriaSerializer(many=True, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   ['id', 'nombre_revista', 'logo', 'cat_revista', 'country', 'state', 'city', 'plan']


#serializador CRUD de revista
class POSTRevistaSerializer(serializers.ModelSerializer):
    plan    =   serializers.PrimaryKeyRelatedField(
                        queryset=PlanRevista.objects.all(),
                        required=False,
                        many=False)
    country =   serializers.PrimaryKeyRelatedField(
                        queryset=Region.objects.all(),
                        required=False,
                        many=True)
    state   =   serializers.PrimaryKeyRelatedField(
                        queryset=Subregion.objects.all(),
                        required=False,
                        many=True)
    city    =   serializers.PrimaryKeyRelatedField(
                        queryset=Ciudad.objects.all(),
                        required=False,
                        many=True)
    class Meta:
        model   =   Revista
        fields  =   '__all__'


#serializador para CRUD de categoria
class POSTCategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   serializers.PrimaryKeyRelatedField(
                        queryset=Revista.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

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

