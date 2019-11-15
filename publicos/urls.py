from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

router.register('Lista-articulos',ArticuloList)
router.register('Lista-especiales',EspecialArticuloList)
router.register('Lista-cotizaciones',CotizacionesList)
router.register('Lista-planes',PlanList)
router.register('Lista-paises',PaisViewSet)
router.register('Lista-estados',EstadoViewSet)
router.register('Lista-ciudades',CiudadViewSet)
router.register('Lista-categorias',CategoriaRevistaList)
router.register('Lista-subcategorias',SubcategoriaRevistaList)

publicos = [
    url('publicos/', include(router.urls)),
]