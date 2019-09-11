from rest_framework import serializers
from .models import Articulo
from revista.serializers import NomCategoriaSerializer, NomRevistaSerializer

class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

class EspecialArticulo(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['slug','en_portada','origen_revista','titulo','categoria','imagen_destacada_uno','status','fecha_fin']