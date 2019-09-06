from rest_framework import serializers
from .models import *
from revista.serializers import SoloRevistaSerializer

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   '__all__'

class SoloPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   ['nombre']

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Forma_Pago
        fields  =   '__all__'

class NomFormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Forma_Pago
        fields  =   ['nombre']


class ContratoSerializer(serializers.ModelSerializer):
    revista     = SoloRevistaSerializer(many=False, read_only=True)
    forma_pago  = NomFormaPagoSerializer(many=False, read_only=True)
    class Meta:
        model   =   Contrato
        fields  =   '__all__'