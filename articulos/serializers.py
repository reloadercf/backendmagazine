from rest_framework import serializers
from .models import Articulo
from revista.models import *
from revista.serializers import *
from patrocinadores.models import Patrocinador
from contenido.serializers import DatosContenidoSerializer, ContenidoSerializer


#serializador para sacar nombre de la revista
class NomRevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista']


#serializador para sacar nombre de categoria
class NomCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Categorias
        fields  =   ['id','nombre_categoria', 'icono']

#serializador para sacar nombre de subcategoria
class NomSubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Subcategorias
        fields  =   ['id','nombre_subcategoria']


#serializador para sacar datos de los articulos
class ArticuloSerializer(serializers.ModelSerializer):
    #origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    #con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['id', 'titulo', 'imagen','redactado_por','fecha_publicacion','categoria', 'subcategoria', 'slug']



#Detalle Articulo
class DetalleArticuloSerializer(serializers.ModelSerializer):
    #origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   ContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['id', 'titulo', 'imagen', 'con_art','redactado_por','fecha_publicacion','categoria', 'subcategoria', 'slug']



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
    #origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    #con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['id','titulo','imagen','en_portada','categoria','subcategoria', 'redactado_por','cortesia_de','fecha_publicacion','slug']
    
#serializador de sacar datos para revista
# class DatosArticuloSerializer(serializers.ModelSerializer):
#     categoria       =   NomCategoriaSerializer(many=False, read_only=True)
#     subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
#     #con_art         =   DatosContenidoSerializer(many=True, read_only=True)
#     class Meta:
#         model       =   Articulo
#         fields      =   ['id','titulo','imagen','en_portada','categoria','subcategoria', 'redactado_por','cortesia_de','fecha_publicacion','slug']