from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

router.register('Registro-de-planes',PlanViewSet)
router.register('Registro-de-formas-de-pago',FormaPagoViewSet)
router.register('Lista-de-contratos',ContratoViewSet)
router.register('Registro-de-contratos',POSTContratoViewSet)

planes = [
    url('planes/', include(router.urls)),
]