from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from .pagination import ArticlePagination
from django.db.models import Q
from datetime import *

#vista para visualizacion de datos de articulos
class ArticuloViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Articulo.objects.all().order_by('-fecha_publicacion')
    serializer_class = ArticuloSerializer
    pagination_class = ArticlePagination
    def get_queryset(self,*args,**kwargs):
        categoria       =   self.request.GET.get("idcategoria")
        subcategoria    =   self.request.GET.get("idsubcategoria")
        origen_revista  =   self.request.GET.get("idrevista")
        slug            =   self.request.GET.get("slug")
        fin             =   self.request.GET.get("fin")
        inicio          =   self.request.GET.get("inicio")
        portada         =   self.request.GET.get("portada")
        queryset_list = super(ArticuloViewSet, self).get_queryset()
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
        return queryset_list

#vista para CRUD de datos de articulo
class POSTArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = POSTArticuloSerializer

#vista para visualizacion de datos de articulos especiales
class EspecialArticuloViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Articulo.objects.all().order_by('-fecha_publicacion')
    serializer_class = EspecialArticuloSerializer
    def get_queryset(self,*args,**kwargs):
        categoria       =       self.request.GET.get("idcategoria")
        subcategoria    =       self.request.GET.get("idsubcategoria")
        origen_revista  =       self.request.GET.get("idrevista")
        slug            =       self.request.GET.get("slug")
        portada         =       self.request.GET.get("portada")
        status          =       self.request.GET.get("status")
        queryset_list = super(EspecialArticuloViewSet, self).get_queryset()
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
        if status:
            queryset_list = queryset_list.filter(status=status)
        return queryset_list