from rest_framework import serializers
from revista.models import *
from planrevista.models import *
from patrocinadores.models import *
from articulos.models import *
from accounts.models import *
from regiones.models import *
from revista.serializers import NomPlanSerializer, NomRevistaSerializer, RevistaPlanSerializer, NomCategoriaSerializer, NomSubcategoriaSerializer
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer 
from planrevista.serializers import NomFormaPagoSerializer
from accounts.serializers import ProfileSerializer, ProfileRSerializer

class RevistaSerializer(serializers.ModelSerializer):
    plan    =   NomPlanSerializer(many=False, read_only=True)
    pais    =   NomRegionSerializer(many=False, read_only=True)
    estado  =   NomSubregionSerializer(many=False, read_only=True)
    class Meta:
        model   =   Revista
        fields  =   '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   NomRevistaSerializer(read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    revista     =   RevistaPlanSerializer(many=False, read_only=True)
    forma_pago  =   NomFormaPagoSerializer(many=False, read_only=True)
    class Meta:
        model   =   Contrato
        fields  =   '__all__'

class PatrocinadorSerializer(serializers.ModelSerializer):
    revista_pertenencia =   NomRevistaSerializer(read_only=True)
    plan_contratado     =   NomPlanSerializer(read_only=True)
    class Meta:
        model   =   Patrocinador
        fields  =   '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

class EspecialArticulo(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['slug','en_portada','origen_revista','titulo','categoria','subcategoria','imagen_destacada_uno','status','fecha_fin']

class UserSerializer(serializers.ModelSerializer):
	profile_user	=	ProfileSerializer(many=False, read_only=True)
	password 		=	serializers.CharField(write_only=True)
	class Meta:
		model 	= 	User
		fields 	= 	['first_name', 'last_name', 'email', 'id', 'password', 'profile_user']
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.save()
		return user

class UserRevistaSerializer(serializers.ModelSerializer):
	profile_user = ProfileRSerializer(many=False, read_only=True)
	class Meta:
		model = User
		fields = ['username','profile_user']

class CiudadSerializer(serializers.ModelSerializer):
    estado      =   NomSubregionSerializer(many=False, read_only=True)
    class Meta:
        model   =   Ciudad
        fields  =   '__all__'

class SubregionSerializer(serializers.ModelSerializer):
    pais        =   NomRegionSerializer(many=False, read_only=True)
    class Meta:
        model   =   Subregion
        fields  =   '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Region
        fields  =   '__all__'