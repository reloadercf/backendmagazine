from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#visualizacion de contenidos
router.register('Lista-de-Contenidos',ContenidoViewSet)
#CRUD de contenidos
router.register('Registro-de-Contenidos',POSTContenidoViewSet)

contenido = [
    url('contenido/', include(router.urls)),
]