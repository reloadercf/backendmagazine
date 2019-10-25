from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

router.register('Lista-Articulos',ArticuloList)
router.register('Lista-Especiales',EspecialArticuloList)
router.register('Lista-Cotizaciones',CotizacionesList)
router.register('Lista-Planes',PlanList)
router.register('Lista-Paises',PaisViewSet)
router.register('Lista-Estados',EstadoViewSet)
router.register('Lista-Ciudades',CiudadViewSet)
router.register('Lista-Categorias',CategoriaRevistaList)
router.register('Lista-Subcategorias',SubcategoriaRevistaList)

publicos = [
    url('publicos/', include(router.urls)),
]