from rest_framework import serializers
from .models import Patrocinador
from revista.serializers import NomRevistaSerializer
from revista.serializers import NomPlanSerializer

class PatrocinadorSerializer(serializers.ModelSerializer):
    revista_pertenencia =   NomRevistaSerializer(read_only=True)
    plan_contratado     =   NomPlanSerializer(read_only=True)
    class Meta:
        model   =   Patrocinador
        fields  =   '__all__'
