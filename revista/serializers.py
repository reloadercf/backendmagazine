from rest_framework import serializers
from .models import Categorias,Revista
from planrevista.serializers import SoloPlanSerializer


class NomCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Categorias
        fields  =   ['nombre_categoria']

# class RevistaSerializer(serializers.ModelSerializer):
#     #plan = SoloPlanSerializer(many=False, read_only=True)
#     class Meta:
#         model   =   Revista
#         fields  =   '__all__'

# class NomRevistaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model   =   Revista
#         fields  =   ['nombre_revista']



# class SoloRevistaSerializer(serializers.ModelSerializer):
#     #plan = SoloPlanSerializer(many=False, read_only=True)
#     class Meta:
#         model   =   Revista
#         fields  =   ['nombre_revista','plan']

# class CategoriaSerializer(serializers.ModelSerializer):
#     revista_origen=NomRevistaSerializer(read_only=True)
#     class Meta:
#         model       =   Categorias
#         fields      =   '__all__'