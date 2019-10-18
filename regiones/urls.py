from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#visualizacion de CRUD de paises
router.register('Registro-de-paises',PaisViewSet)
#visualizacion de CRUD de estados
router.register('Registro-de-estados',POSTEstadoViewSet)
#visualizacion de datos de estados
router.register('Lista-de-estados',EstadoViewSet)
#visualizacion de CRUD de ciudades
router.register('Registro-de-ciudades',POSTCiudadViewSet)
#visualizacion de datos de ciudades
router.register('Lista-de-ciudades',CiudadViewSet)

regiones = [
    url('regiones/', include(router.urls)),
]