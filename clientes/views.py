from django.shortcuts import render
from .models import Cliente
from .serializers import ClieteSerializer
from rest_framework import viewsets
from .pagination import ClientePagination
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset            =   Cliente.objects.all()
    serializer_class    =   ClieteSerializer
    pagination_class    =   ClientePagination
    def get_queryset(self, *args, **kwargs):
        cliente = self.request.GET.get('idcliente')
        revista = self.request.GET.get('idrevista')
        queryset_list = super(ClienteViewSet, self).get_queryset()
        if cliente:
            queryset_list = queryset_list.filter(id=cliente)
        if revista:
            queryset_list = queryset_list.filter(revista_pertenencia=revista)
        return queryset_list