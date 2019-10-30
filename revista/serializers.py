from rest_framework import serializers
from .models import Categorias,Revista, Subcategorias, Icon
from planrevista.serializers import NomPlanSerializer
from planrevista.models import PlanRevista
from patrocinadores.serializers import DatosPatrocinadorSerializer
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer, NomCiudadSerializer
from articulos.serializers import NomRevistaSerializer, NomCategoriaSerializer, DatosArticuloSerializer
from regiones.models import *
from accounts.models import Profile
from django.core.paginator import Paginator

#serializador para sacar datos de la revista
class RevistaSerializer(serializers.ModelSerializer):
    plan        =   NomPlanSerializer(many=False, read_only=True)
    country     =   NomRegionSerializer(many=False, read_only=True)
    state       =   NomSubregionSerializer(many=False, read_only=True)
    city        =   NomCiudadSerializer(many=False, read_only=True)
    art_revista =   serializers.SerializerMethodField('paginated_art') #forma de definir paginacion a un atributo
    pat_revista =   serializers.SerializerMethodField('paginated_pat') #forma de definir paginacion a un atributo
    class Meta:
        model   =   Revista
        fields  =   '__all__'
#funcion para paginar la cantidad de articulos de la revista
    def paginated_art(self, obj): 
        paginator = Paginator(obj.art_revista.all(), 2) #pagina los objetos y la cantidad a mostrar
        art_rev = paginator.page(1) #señala a donde se guardara y que pagina
        serializer = DatosArticuloSerializer(art_rev, many=True) #toma el serializador para paginar
        return serializer.data

#funcion para paginar la cantidad de patrocinadores de la revista
    def paginated_pat(self, obj):
        paginator = Paginator(obj.pat_revista.all(), 2) #pagina los objetos y la cantidad a mostrar
        pat_rev = paginator.page(1) #señala a donde se guardara y que pagina
        serializer = DatosPatrocinadorSerializer(pat_rev, many=True) #toma el serializador para paginar
        return serializer.data

#serializador CRUD de revista
class POSTRevistaSerializer(serializers.ModelSerializer):
    plan    =   serializers.PrimaryKeyRelatedField(
                        queryset=PlanRevista.objects.all(),
                        required=False,
                        many=False)
    country =   serializers.PrimaryKeyRelatedField(
                        queryset=Region.objects.all(),
                        required=False,
                        many=False)
    state   =   serializers.PrimaryKeyRelatedField(
                        queryset=Subregion.objects.all(),
                        required=False,
                        many=False)
    city    =   serializers.PrimaryKeyRelatedField(
                        queryset=Ciudad.objects.all(),
                        required=False,
                        many=False)
    class Meta:
        model   =   Revista
        fields  =   ['id','nombre_revista', 'plan', 'country', 'state', 'city']

#serializador para sacar datos de la categoria
class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   NomRevistaSerializer(many=False, read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

#serializador para CRUD de categoria
class POSTCategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   serializers.PrimaryKeyRelatedField(
                        queryset=Revista.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

#serializador para datos de subcategoria
class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   NomCategoriaSerializer(many=False, read_only=True)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'

#serializador para CRUD de subcategoria
class POSTSubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   serializers.PrimaryKeyRelatedField(
                        queryset=Categorias.objects.all(),
                        required=True,
                        many=False)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields ='__all__'