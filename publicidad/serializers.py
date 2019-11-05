from rest_framework import serializers
from .models import Publicidad
from patrocinadores.models import Patrocinador
from patrocinadores.serializers import NomPatrocinadorSerializer

#serializador para CRUD del modelo publicidad
class POSTPublicidadSerializer(serializers.ModelSerializer):
    patrocinador    =   serializers.PrimaryKeyRelatedField(
                        queryset=Patrocinador.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model   =   Publicidad
        fields  =   '__all__'

#serializador para sacar datos de publicidad
class PublicidadSerializer(serializers.ModelSerializer):
    patrocinador    =   NomPatrocinadorSerializer(read_only=True)
    class Meta:
        model       =   Publicidad
        fields      =   '__all__'