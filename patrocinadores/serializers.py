from rest_framework import serializers
from .models import Patrocinador
from revista.serializers import NomRevistaSerializer, NomPlanSerializer
from revista.models import Revista
from planrevista.models import PlanRevista

#serializador para el nombre del patrocinador
class NomPatrocinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Patrocinador
        fields  =   ['nombre']

#serializador para datos del patrocinador
class PatrocinadorSerializer(serializers.ModelSerializer):
    revista_pertenencia =   NomRevistaSerializer(read_only=True)
    class Meta:
        model   =   Patrocinador
        fields  =   '__all__'

#serializador para CRUD del patrocinador
class POSTPatrocinadorSerializer(serializers.ModelSerializer):
    revista_pertenencia =   serializers.PrimaryKeyRelatedField(
                            queryset=Revista.objects.all(),
                            required=True,
                            many=False)
    class Meta:
        model   =   Patrocinador
        fields  =   '__all__'