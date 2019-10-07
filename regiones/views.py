from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class EstadoViewSet(viewsets.ModelViewSet):
    queryset            =   Subregion.objects.all()
    serializer_class    =   SubregionSerializer
    def get_queryset(self, *args, **kwargs):
        estado=self.request.GET.get('idestado')
        pais=self.request.GET.get('idpais')
        queryset_list=super(EstadoViewSet, self).get_queryset()
        if pais:
            queryset_list=queryset_list.filter(pais__id=pais)
        if estado:
            queryset_list=queryset_list.filter(id=estado)
        return queryset_list

class POSTEstadoViewSet(viewsets.ModelViewSet):
    queryset            =   Subregion.objects.all()
    serializer_class    =   POSTSubegionSerializer
    def get_queryset(self, *args, **kwargs):
        estado=self.request.GET.get('idestado')
        pais=self.request.GET.get('idpais')
        queryset_list=super(POSTEstadoViewSet, self).get_queryset()
        if pais:
            queryset_list=queryset_list.filter(pais__id=pais)
        if estado:
            queryset_list=queryset_list.filter(id=estado)
        return queryset_list

class CiudadViewSet(viewsets.ModelViewSet):
    queryset            =   Ciudad.objects.all()
    serializer_class    =   CiudadSerializer
    def get_queryset(self, *args, **kwargs):
        ciudad=self.request.GET.get('idciudad')
        estado=self.request.GET.get('idestado')
        queryset_list=super(CiudadViewSet, self).get_queryset()
        if ciudad:
            queryset_list=queryset_list.filter(id=ciudad)
        if estado:
            queryset_list=queryset_list.filter(estado__id=estado)
        return queryset_list
    
class POSTCiudadViewSet(viewsets.ModelViewSet):
    queryset            =   Ciudad.objects.all()
    serializer_class    =   POSTCiudadSerializer
    def get_queryset(self, *args, **kwargs):
        ciudad=self.request.GET.get('idciudad')
        estado=self.request.GET.get('idestado')
        queryset_list=super(POSTCiudadViewSet, self).get_queryset()
        if ciudad:
            queryset_list=queryset_list.filter(id=ciudad)
        if estado:
            queryset_list=queryset_list.filter(estado__id=estado)
        return queryset_list

class PaisViewSet(viewsets.ModelViewSet):
    queryset            =   Region.objects.all()
    serializer_class    =   RegionSerializer
    def get_queryset(self, *args, **kwargs):
        pais=self.request.GET.get('idpais')
        queryset_list=super(PaisViewSet, self).get_queryset()
        if pais:
            queryset_list=queryset_list.filter(id=pais)
        return queryset_list