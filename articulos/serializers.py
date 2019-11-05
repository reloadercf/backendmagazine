from rest_framework import serializers
from .models import Articulo
from revista.models import *
from patrocinadores.models import Patrocinador
from contenido.serializers import DatosContenidoSerializer

#serializador para sacar nombre de la revista
class NomRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']

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

#serializador para sacar datos de los articulos
class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   DatosContenidoSerializer(many=True, read_only=True)
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
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

#serializador para sacar datos de articulos especiales
class EspecialArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['slug','en_portada','origen_revista','titulo','categoria','subcategoria','imagen','con_art','publicado','fecha_fin']
    
#serializador de sacar datos para revista
class DatosArticuloSerializer(serializers.ModelSerializer):
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['titulo','en_portada','categoria','subcategoria','imagen','con_art','redactado_por','publicado','cortesia_de','fecha_publicacion','fecha_fin','fecha_creacion','fecha_modificacion','slug']