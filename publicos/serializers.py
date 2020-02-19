from rest_framework import serializers
from revista.models import *
from planrevista.models import *
from patrocinadores.models import *
from articulos.models import *
from accounts.models import *
from regiones.models import *
#from cotizador.models import *
from articulos.serializers import NomRevistaSerializer, NomCategoriaSerializer, NomSubcategoriaSerializer
from regiones.serializers import NomRegionSerializer, NomSubregionSerializer 
from planrevista.serializers import NomFormaPagoSerializer, RevistaPlanSerializer, NomPlanSerializer
from accounts.serializers import ProfileSerializer
from contenido.serializers import DatosContenidoSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    revista_origen  =   NomRevistaSerializer(read_only=True)
    class Meta:
        model       =   Categorias
        fields      =   '__all__'

class PlanRSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   PlanRevista
        fields  =   '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   '__all__'

class EspecialArticuloSerializer(serializers.ModelSerializer):
    origen_revista  =   NomRevistaSerializer(many=False, read_only=True)
    categoria       =   NomCategoriaSerializer(many=False, read_only=True)
    subcategoria    =   NomSubcategoriaSerializer(many=False, read_only=True)
    con_art         =   DatosContenidoSerializer(many=True, read_only=True)
    class Meta:
        model       =   Articulo
        fields      =   ['slug','en_portada','origen_revista','titulo','categoria','subcategoria','imagen','con_art','publicado','fecha_fin']

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

class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria   =   NomCategoriaSerializer(many=False, read_only=True)
    class Meta:
        model   =   Subcategorias
        fields  =   '__all__'

# class CotizacionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model   =   Cotizador
#         fields  =   '__all__'