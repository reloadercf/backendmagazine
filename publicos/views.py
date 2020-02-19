from rest_framework import viewsets
from publicos.serializers import *
from django.db.models import Q

# class CotizacionesList(viewsets.ReadOnlyModelViewSet):
#     queryset = Cotizador.objects.all()
#     serializer_class = CotizacionSerializer

class CategoriaRevistaList(viewsets.ReadOnlyModelViewSet):
    queryset            =   Categorias.objects.all()
    serializer_class    =   CategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria   = self.request.GET.get('idcategoria')
        revista     = self.request.GET.get('idrevista')
        nombre      = self.request.GET.get('nombre')  
        queryset_list = super(CategoriaRevistaList, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_categoria__contains=nombre)
            )
        if categoria:
            queryset_list = queryset_list.filter(id=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista_origen_id=revista)
        return queryset_list

class SubcategoriaRevistaList(viewsets.ReadOnlyModelViewSet):
    queryset            =   Subcategorias.objects.all()
    serializer_class    =   SubcategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria       = self.request.GET.get('idcategoria')
        subcategoria    = self.request.GET.get('idsubcategoria')
        nombre          = self.request.GET.get('nombre')  
        queryset_list = super(SubcategoriaRevistaList, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_subcategoria__contains=nombre)
            )
        if categoria:
            queryset_list = queryset_list.filter(categoria__id=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(id=subcategoria)
        return queryset_list

class PlanList(viewsets.ReadOnlyModelViewSet):
    queryset            =   PlanRevista.objects.all()
    serializer_class    =   PlanRSerializer


class ArticuloList(viewsets.ReadOnlyModelViewSet):
    queryset = Articulo.objects.all().order_by('-fecha_publicacion')
    serializer_class = ArticuloSerializer
    def get_queryset(self,*args,**kwargs):
        categoria       =   self.request.GET.get("idcategoria")
        subcategoria    =   self.request.GET.get("idsubcategoria")
        origen_revista  =   self.request.GET.get("idrevista")
        slug            =   self.request.GET.get("slug")
        fin             =   self.request.GET.get("fin")
        inicio          =   self.request.GET.get("inicio")
        portada         =   self.request.GET.get("portada")
        publicado       =       self.request.GET.get("publicado")
        queryset_list = super(ArticuloList, self).get_queryset()
        if origen_revista:
            queryset_list = queryset_list.filter(origen_revista__id=origen_revista)
        if categoria:
            queryset_list = queryset_list.filter(categoria__id=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(subcategoria__id=subcategoria)
        if fin:
            queryset_list = queryset_list.filter(fecha_fin=fin)
        if inicio:
            queryset_list = queryset_list.filter(fecha_publicacion=inicio)
        if slug:
            queryset_list = queryset_list.filter(slug=slug)
        if portada:
            queryset_list = queryset_list.filter(en_portada=portada)
        if publicado:
            queryset_list = queryset_list.filter(publicado=publicado)
        return queryset_list

class EspecialArticuloList(viewsets.ReadOnlyModelViewSet):
    queryset = Articulo.objects.all().order_by('-fecha_publicacion')
    serializer_class = EspecialArticuloSerializer
    def get_queryset(self,*args,**kwargs):
        categoria       =       self.request.GET.get("idcategoria")
        subcategoria    =       self.request.GET.get("idsubcategoria")
        origen_revista  =       self.request.GET.get("idrevista")
        slug            =       self.request.GET.get("slug")
        portada         =       self.request.GET.get("portada")
        publicado       =       self.request.GET.get("publicado")
        queryset_list = super(EspecialArticuloList, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria__id=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(categoria__id=subcategoria)
        if origen_revista:
            queryset_list = queryset_list.filter(origen_revista__id=origen_revista)
        if slug:
            queryset_list = queryset_list.filter(slug=slug)
        if portada:
            queryset_list = queryset_list.filter(en_portada=portada)
        if publicado:
            queryset_list = queryset_list.filter(publicado=publicado)
        return queryset_list

class PaisList(viewsets.ReadOnlyModelViewSet):
    queryset            =   Region.objects.all()
    serializer_class    =   RegionSerializer

class CiudadList(viewsets.ReadOnlyModelViewSet):
    queryset            =   Ciudad.objects.all()
    serializer_class    =   CiudadSerializer
    def get_queryset(self, *args, **kwargs):
        ciudad=self.request.GET.get('idciudad')
        estado=self.request.GET.get('idestado')
        nombre  =   self.request.GET.get('nombre')
        queryset_list=super(CiudadList, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_ciudad__contains=nombre)
            )
        if ciudad:
            queryset_list=queryset_list.filter(id=ciudad)
        if estado:
            queryset_list=queryset_list.filter(estado__id=estado)
        return queryset_list

class EstadoList(viewsets.ReadOnlyModelViewSet):
    queryset            =   Subregion.objects.all()
    serializer_class    =   SubregionSerializer
    def get_queryset(self, *args, **kwargs):
        estado  =   self.request.GET.get('idestado')
        pais    =   self.request.GET.get('idpais')
        nombre  =   self.request.GET.get('nombre')
        queryset_list=super(EstadoList, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_estado__contains=nombre)
            )
        if pais:
            queryset_list=queryset_list.filter(pais__id=pais)
        if estado:
            queryset_list=queryset_list.filter(id=estado)
        return queryset_list