from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#visualizacion de articulos
router.register('Lista-de-articulos',ArticuloViewSet)
#Detalle Articulo ViewSet
router.register('Detalle-articulo', ArticuloDetalleViewSet)
#visualizacion de articulos especiales
router.register('Lista-de-especiales',EspecialArticuloViewSet)
#CRUD de articulos
router.register('Registro-de-articulos',POSTArticuloViewSet)

articulo = [
    url('articulos/', include(router.urls)),
]