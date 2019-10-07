from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

router.register('Lista-de-estados',EstadoViewSet)
router.register('Lista-de-ciudades',CiudadViewSet)
router.register('Registro-de-paises',PaisViewSet)
router.register('Registro-de-estados',POSTEstadoViewSet)
router.register('Registro-de-ciudades',POSTCiudadViewSet)

regiones = [
    url('regiones/', include(router.urls)),
]