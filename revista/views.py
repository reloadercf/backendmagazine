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
        queryset_list = super(RevistaViewSet, self).get_queryset()
        if revista:
            queryset_list = queryset_list.filter(id=revista)
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