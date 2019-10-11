from rest_framework import serializers
from .models import Patrocinador
from revista.serializers import NomRevistaSerializer, NomPlanSerializer
from revista.models import Revista
from planrevista.models import PlanRevista

class NomPatrocinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Patrocinador
        fields  =   ['nombre']

class PatrocinadorSerializer(serializers.ModelSerializer):
    revista_pertenencia =   NomRevistaSerializer(read_only=True)
    class Meta:
        model   =   Patrocinador
        fields  =   '__all__'

class POSTPatrocinadorSerializer(serializers.ModelSerializer):
    revista_pertenencia =   serializers.PrimaryKeyRelatedField(
                            queryset=Revista.objects.all(),
                            required=True,
                            many=False)
    class Meta:
        model   =   Patrocinador
        fields  =   '__all__'