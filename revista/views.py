from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class RevistaViewSet(viewsets.ModelViewSet):
    queryset=Revista.objects.all()
    serializer_class=RevistaSerializer
    def get_queryset(self, *args, **kwargs):
        revista = self.request.GET.get('idrevista')
        plan    = self.request.GET.get('idplan')
        estado  = self.request.GET.get('idestado')
        pais    = self.request.GET.get('idpais')
        queryset_list = super(RevistaViewSet, self).get_queryset()
        if revista:
            queryset_list = queryset_list.filter(id=revista)
        if plan:
            queryset_list = queryset_list.filter(plan__id=plan)
        if estado:
            queryset_list = queryset_list.filter(estado__id=estado)
        if pais:
            queryset_list = queryset_list.filter(pais__id=pais)
        return queryset_list

class POSTRevistaViewSet(viewsets.ModelViewSet):
    queryset=Revista.objects.all()
    serializer_class=POSTRevistaSerializer
    def get_queryset(self, *args, **kwargs):
        revista = self.request.GET.get('idrevista')
        plan    = self.request.GET.get('idplan')
        estado  = self.request.GET.get('idestado')
        pais    = self.request.GET.get('idpais')
        queryset_list = super(POSTRevistaViewSet, self).get_queryset()
        if revista:
            queryset_list = queryset_list.filter(id=revista)
        if plan:
            queryset_list = queryset_list.filter(plan__id=plan)
        if estado:
            queryset_list = queryset_list.filter(estado__id=estado)
        if pais:
            queryset_list = queryset_list.filter(pais__id=pais)
        return queryset_list

class CategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Categorias.objects.all()
    serializer_class    =   CategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria = self.request.GET.get('idcategoria')
        revista = self.request.GET.get('idrevista')
        queryset_list = super(CategoriaRevistaViewSet, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(id=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista_origen=revista)
        return queryset_list

class POSTCategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Categorias.objects.all()
    serializer_class    =   POSTCategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria = self.request.GET.get('idcategoria')
        revista = self.request.GET.get('idrevista')
        queryset_list = super(POSTCategoriaRevistaViewSet, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(id=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista_origen=revista)
        return queryset_list

class SubcategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Subcategorias.objects.all()
    serializer_class    =   SubcategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria       = self.request.GET.get('idcategoria')
        subcategoria    = self.request.GET.get('idsubcategoria')
        queryset_list = super(SubcategoriaRevistaViewSet, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria__id=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(id=subcategoria)
        return queryset_list

class POSTSubcategoriaRevistaViewSet(viewsets.ModelViewSet):
    queryset            =   Subcategorias.objects.all()
    serializer_class    =   POSTSubcategoriaSerializer
    def get_queryset(self, *args, **kwargs):
        categoria       = self.request.GET.get('idcategoria')
        subcategoria    = self.request.GET.get('idsubcategoria')
        queryset_list = super(POSTSubcategoriaRevistaViewSet, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria__id=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(id=subcategoria)
        return queryset_list