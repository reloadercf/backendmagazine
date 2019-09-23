from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()

router.register('Lista-Revistas',RevistaList)
router.register('Lista-Categorias',CategoriaRevistaList)
router.register('Lista-Planes',PlanList)
router.register('Lista-Contratos',ContratoList)
router.register('Lista-Patrocinadores',PatrocinadorList)
router.register('Lista-Articulos',ArticuloList)
router.register('Lista-Especiales',EspecialArticuloList)
router.register('Lista-Perfiles',ProfileList)
router.register('Lista-Usuario_Revista',UserRevistaList)

publicos = [
    path('publicos/', include(router.urls)),
]