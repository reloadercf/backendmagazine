from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Q
from datetime import *

#vista para CRUD de cotizaciones
class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizador.objects.all()
    serializer_class = CotizacionSerializer