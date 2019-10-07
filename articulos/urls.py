from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
router.register('Lista-de-articulos',ArticuloViewSet)
router.register('Lista-de-especiales',EspecialArticuloViewSet)
router.register('Registro-de-articulos',POSTArticuloViewSet)
router.register('Registro-de-especiales',POSTEspecialArticuloViewSet)

articulo = [
    url('articulo/', include(router.urls)),
]