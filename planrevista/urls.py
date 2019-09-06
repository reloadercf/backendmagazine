from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

router.register('registro-de-planes',PlanViewSet)
router.register('registro-de-formas-de-pago',FormaPagoViewSet)
router.register('registro-de-contratos',ContratoViewSet)

planes = [
    path('planes/', include(router.urls)),
]