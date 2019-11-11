from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Q 

#vista para visualizacion de datos de publicidades
class PublicidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publicidad.objects.all()
    serializer_class = PublicidadSerializer
    def get_queryset(self,*args,**kwargs):
        publicidad      =   self.request.GET.get("idpublicidad")
        patrocinador    =   self.request.GET.get("idpatrocinador")
        nombre          =   self.request.GET.get("nombre")
        queryset_list = super(PublicidadViewSet, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre__contains=nombre)
            )
        if patrocinador:
            queryset_list = queryset_list.filter(patrocinador__id=patrocinador)
        if publicidad:
            queryset_list = queryset_list.filter(id=publicidad)
        return queryset_list

#vista para CRUD de datos de publicidades
class POSTPublicidadViewSet(viewsets.ModelViewSet):
    queryset = Publicidad.objects.all()
    serializer_class = POSTPublicidadSerializer