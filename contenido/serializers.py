from rest_framework import serializers
from .models import Contenido
from articulos.models import Articulo
from articulos.serializers import NomArticuloSerializer

#serializador para CRUD del modelo contenido
class POSTContenidoSerializer(serializers.ModelSerializer):
    articulo    =   serializers.PrimaryKeyRelatedField(
                        queryset=Articulo.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model   =   Contenido
        fields  =   '__all__'

#serializador para sacar datos de contenidos
class ContenidoSerializer(serializers.ModelSerializer):
    articulo  =   NomArticuloSerializer(read_only=True)
    class Meta:
        model       =   Contenido
        fields      =   '__all__'