from django.shortcuts import render
from .models import Patrocinador
from .serializers import PatrocinadorSerializer
from rest_framework import viewsets
from .pagination import PatrocinadorPagination
# Create your views here.

class PatrocinadorViewSet(viewsets.ModelViewSet):
    queryset            =   Patrocinador.objects.all()
    serializer_class    =   PatrocinadorSerializer
    pagination_class    =   PatrocinadorPagination
    def get_queryset(self, *args, **kwargs):
        patrocinador = self.request.GET.get('idpatrocinador')
        revista      = self.request.GET.get('idrevista')
        queryset_list = super(PatrocinadorViewSet, self).get_queryset()
        if patrocinador:
            queryset_list = queryset_list.filter(id=patrocinador)
        if revista:
            queryset_list = queryset_list.filter(revista_pertenencia=revista)
        return queryset_list