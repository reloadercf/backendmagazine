from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class PlanViewSet(viewsets.ModelViewSet):
    queryset            =   PlanRevista.objects.all()
    serializer_class    =   PlanSerializer
    def get_queryset(self, *args, **kwargs):
        plan=self.request.GET.get('idplan')
        queryset_list=super(PlanViewSet, self).get_queryset()
        if plan:
            queryset_list=queryset_list.filter(id=plan)
        return queryset_list

class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset            =   Forma_Pago.objects.all()
    serializer_class    =   FormaPagoSerializer

class ContratoViewSet(viewsets.ModelViewSet):
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
            queryset_list=queryset_list.filter(revista=revista)
        if pago:
            queryset_list=queryset_list.filter(forma_pago=pago)
        if fecha:
            queryset_list=queryset_list.filter(fecha_inicio=fecha)
        return queryset_list