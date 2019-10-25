from rest_framework import serializers
from .models import Articulo
from revista.serializers import NomCategoriaSerializer, NomRevistaSerializer, NomSubcategoriaSerializer
from revista.models import *
from patrocinadores.models import Patrocinador
from patrocinadores.serializers import NomPatrocinadorSerializer

#serializador para sacar datos de los articulos
class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    patrocinador    =   NomPatrocinadorSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

#serializador para CRUD de articulos
class POSTArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   serializers.PrimaryKeyRelatedField(
                        queryset=Revista.objects.all(),
                        required=True,
                        many=False)
    categoria       =   serializers.PrimaryKeyRelatedField(
                        queryset=Categorias.objects.all(),
                        required=True,
                        many=False)
    subcategoria    =   serializers.PrimaryKeyRelatedField(
                        queryset=Subcategorias.objects.all(),
                        required=True,
                        many=False)
    patrocinador    =   serializers.PrimaryKeyRelatedField(
                        queryset=Patrocinador.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

#serializador para sacar datos de articulos especiales
class EspecialArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['slug','en_portada','origen_revista','titulo','categoria','subcategoria','imagen_destacada_uno','status','fecha_fin']