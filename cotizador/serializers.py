from rest_framework import serializers
from .models import Cotizador

#serializador para CRUD del modelo cotizador
class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Cotizador
        fields  =   '__all__'