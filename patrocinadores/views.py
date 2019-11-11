from django.shortcuts import render
from .models import Patrocinador
from .serializers import *
from rest_framework import viewsets
from .pagination import PatrocinadorPagination
from django.db.models import Q

#vista para datos de patrocinadores
class PatrocinadorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            =   Patrocinador.objects.all()
    serializer_class    =   PatrocinadorSerializer
    pagination_class    =   PatrocinadorPagination
    def get_queryset(self, *args, **kwargs):
        patrocinador    = self.request.GET.get('idpatrocinador')
        revista         = self.request.GET.get('idrevista')
        nombre          = self.request.GET.get('nombre')
        queryset_list = super(PatrocinadorViewSet, self).get_queryset()
        if nombre:
            queryset_list = queryset_list.filter(
				Q(nombre__contains=nombre)
            )
        if patrocinador:
            queryset_list = queryset_list.filter(id=patrocinador)
        if revista:
            queryset_list = queryset_list.filter(revista_pertenencia=revista)
        return queryset_list

#vista para CRUD de patrocinadores
class POSTPatrocinadorViewSet(viewsets.ModelViewSet):
    queryset            =   Patrocinador.objects.all()
    serializer_class    =   POSTPatrocinadorSerializer