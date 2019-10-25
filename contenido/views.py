from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

#vista para visualizacion de datos de contenidos
class ContenidoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
    def get_queryset(self,*args,**kwargs):
        articulo    =   self.request.GET.get("idarticulo")
        contenido   =   self.request.GET.get("idcontenido")
        tipo        =   self.request.GET.get("tipo")
        queryset_list = super(ContenidoViewSet, self).get_queryset()
        if articulo:
            queryset_list = queryset_list.filter(articulo__id=articulo)
        if contenido:
            queryset_list = queryset_list.filter(id=contenido)
        if tipo:
            queryset_list = queryset_list.filter(tipo=tipo)
        return queryset_list

#vista para CRUD de datos de contenido
class POSTContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = POSTContenidoSerializer