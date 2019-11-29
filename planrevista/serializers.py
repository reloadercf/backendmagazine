from rest_framework import serializers
from .models import *

#serializador para sacar nombre de plan de la revista
class NomPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   ['id','nombre']

#serializador para sacar nombre de plan y de la revista
class RevistaPlanSerializer(serializers.ModelSerializer):
    plan    =   NomPlanSerializer(many=False, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   ['nombre_revista','plan']

#serializador CRUD de planes
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   '__all__'

#serializador CRUD de formas de pago
class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Forma_Pago
        fields  =   '__all__'

#serializador para sacar nmbre de formas de pago
class NomFormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Forma_Pago
        fields  =   ['nombre']

#serializador datos de contratos
class ContratoSerializer(serializers.ModelSerializer):
    revista     =   RevistaPlanSerializer(many=False, read_only=True)
    forma_pago  =   NomFormaPagoSerializer(many=False, read_only=True)
    class Meta:
        model   =   Contrato
        fields  =   '__all__'

#serializador CRUD de contratos
class POSTContratoSerializer(serializers.ModelSerializer):
    revista     =   serializers.PrimaryKeyRelatedField(
                    queryset=Revista.objects.all(),
                    required=True,
                    many=False)
    forma_pago  =   serializers.PrimaryKeyRelatedField(
                    queryset=Forma_Pago.objects.all(),
                    required=True,
                    many=False)
    class Meta:
        model   =   Contrato
        fields  =   '__all__'