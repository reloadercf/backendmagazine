from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Q

#vista CRUD de planes
class PlanViewSet(viewsets.ModelViewSet):
    queryset            =   PlanRevista.objects.all()
    serializer_class    =   PlanSerializer

#vista CRUD de formas de pago
class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset            =   Forma_Pago.objects.all()
    serializer_class    =   FormaPagoSerializer

#vista de datos de contratos
class ContratoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            =   Contrato.objects.all()
    serializer_class    =   ContratoSerializer
    def get_queryset(self, *args, **kwargs):
        contrato = self.request.GET.get('idcontrato')
        revista = self.request.GET.get('idrevista')
        pago = self.request.GET.get('idpago')
        fecha = self.request.GET.get('inicio')
        queryset_list=super(ContratoViewSet, self).get_queryset()
        if contrato:
            queryset_list=queryset_list.filter(id=contrato)
        if revista:
            queryset_list=queryset_list.filter(revista__id=revista)
        if pago:
            queryset_list=queryset_list.filter(forma_pago__id=pago)
        if fecha:
            queryset_list=queryset_list.filter(fecha_inicio=fecha)
        return queryset_list

#vista CRUD de contratos
class POSTContratoViewSet(viewsets.ModelViewSet):
    queryset            =   Contrato.objects.all()
    serializer_class    =   POSTContratoSerializer