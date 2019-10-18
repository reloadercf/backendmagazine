from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#visualizacion de articulos
router.register('Lista-de-articulos',ArticuloViewSet)
#visualizacion de articulos especiales
router.register('Lista-de-especiales',EspecialArticuloViewSet)
#CRUD de articulos
router.register('Registro-de-articulos',POSTArticuloViewSet)
#CRUD de iconos
router.register('Registro-de-iconos',IconViewSet)

articulo = [
    url('articulo/', include(router.urls)),
]