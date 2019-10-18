from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#CRUD de articulos
router.register('Registro-de-cotizaciones',CotizacionViewSet)

cotizacion = [
    url('cotizacion/', include(router.urls)),
]