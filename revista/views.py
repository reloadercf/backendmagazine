from django.shortcuts import render
from .models import *
from articulos.models import Articulo
from .serializers import *
from .serializers import RevistaDetalleSerializer
from rest_framework import viewsets
from django.db.models import Prefetch
from django.db.models import Q

#vista de datos de revista
class RevistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Revista.objects.prefetch_related(Prefetch('art_revista',
        queryset=Articulo.objects.order_by('-fecha_publicacion')))
    serializer_class=RevistaSerializer
    def get_queryset(self, *args, **kwargs):
        revista = self.request.GET.get('idrevista')
        plan    = self.request.GET.get('idplan')
        estado  = self.request.GET.get('idestado')
        pais    = self.request.GET.get('idpais')
        ciudad  = self.request.GET.get('idciudad')
        nombre  = self.request.GET.get('nombre')  
        queryset_list = super(RevistaViewSet, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_revista__contains=nombre)
            )
        if revista:
            queryset_list = queryset_list.filter(id=revista)
        if plan:
            queryset_list = queryset_list.filter(plan__id=plan)
        if estado:
            queryset_list = queryset_list.filter(estado__id=estado)
        if pais:
            queryset_list = queryset_list.filter(pais__id=pais)
        if ciudad:
            queryset_list = queryset_list.filter(ciudad__id=ciudad)
        return queryset_list

#vista de CRUD de revista
class POSTRevistaViewSet(viewsets.ModelViewSet):
    queryset=Revista.objects.all()
    serializer_class=POSTRevistaSerializer
class DetalleRevistaViewSet(viewsets.ModelViewSet):
    queryset=Revista.objects.all()
    serializer_class=RevistaDetalleSerializer

#vista de datos de categoria
class CategoriaRevistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            =   Categorias.objects.all()
    serializer_class    =   CategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria   = self.request.GET.get('idcategoria')
        revista     = self.request.GET.get('idrevista')
        nombre      = self.request.GET.get('nombre')  
        queryset_list = super(CategoriaRevistaViewSet, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_categoria__contains=nombre)
            )
        if categoria:
            queryset_list = queryset_list.filter(id=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista_origen_id=revista)
        return queryset_list

#vista de CRUD de categoria
class POSTCategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Categorias.objects.all()
    serializer_class    =   POSTCategoriaSerializer

#vista de datos de subcategoria
class SubcategoriaRevistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            =   Subcategorias.objects.all()
    serializer_class    =   SubcategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria       = self.request.GET.get('idcategoria')
        subcategoria    = self.request.GET.get('idsubcategoria')
        nombre          = self.request.GET.get('nombre')  
        queryset_list = super(SubcategoriaRevistaViewSet, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre_subcategoria__contains=nombre)
            )
        if categoria:
            queryset_list = queryset_list.filter(categoria__id=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(id=subcategoria)
        return queryset_list

#vista de CRUD de subcategoria
class POSTSubcategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Subcategorias.objects.all()
    serializer_class    =   POSTSubcategoriaSerializer

