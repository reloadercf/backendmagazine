from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#visualizacion de publicidades
router.register('Lista-de-Publicidades',PublicidadViewSet)
#CRUD de publicidades
router.register('Registro-de-Publicidades',POSTPublicidadViewSet)

publicidad = [
    url('publicidades/', include(router.urls)),
]