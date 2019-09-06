from rest_framework import serializers
from .models import Cliente
from revista.serializers import NomRevistaSerializer
from planrevista.serializers import SoloPlanSerializer

class ClieteSerializer(serializers.ModelSerializer):
    revista_pertenencia = NomRevistaSerializer(read_only=True)
    plan_contratado = SoloPlanSerializer(read_only=True)
    class Meta:
        model   =   Cliente
        fields  =   '__all__'
