from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

#visualizacion CRUD de planes
router.register('Registro-de-planes',PlanViewSet)
#visualizacion CRUD de formas de pago
router.register('Registro-de-formas-de-pago',FormaPagoViewSet)
#visualizacion CRUD de contratos
router.register('Registro-de-contratos',POSTContratoViewSet)
#visualizacion de datos de contratos
router.register('Lista-de-contratos',ContratoViewSet)

planes = [
    url('planes/', include(router.urls)),
]