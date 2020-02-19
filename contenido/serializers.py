from rest_framework import serializers
from .models import Contenido
from articulos.models import Articulo

#serializador para sacar nombre de los articulos
class NomArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   Articulo
        fields      =   ['titulo']

#serializador para sacar para serializador de articulos
class DatosContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model       =   Contenido
        fields      =   ['tipo','recurso','alt']


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
        exclude      =  ['articulo']
