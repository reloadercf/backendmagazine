from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

#vista de datos de estados
class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
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

#vista de CRUD de estados
class POSTEstadoViewSet(viewsets.ModelViewSet):
    queryset            =   Subregion.objects.all()
    serializer_class    =   POSTSubegionSerializer

#vista de datos de ciudades
class CiudadViewSet(viewsets.ReadOnlyModelViewSet):
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
    
#vista de CRUD de ciudades
class POSTCiudadViewSet(viewsets.ModelViewSet):
    queryset            =   Ciudad.objects.all()
    serializer_class    =   POSTCiudadSerializer

#vista de CRUD de paises
class PaisViewSet(viewsets.ModelViewSet):
    queryset            =   Region.objects.all()
    serializer_class    =   RegionSerializer