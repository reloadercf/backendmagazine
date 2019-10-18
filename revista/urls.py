from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#Visualizacion CRUD de revista
router.register('Registro-de-revistas',POSTRevistaViewSet)
#Visualizacion de datos de revista
router.register('Lista-de-revista',RevistaViewSet)
#Visualizacion CRUD de categoria
router.register('Registro-de-categorias',POSTCategoriaRevistaViewSet)
#Visualizacion de datos de categoria
router.register('Lista-de-categoria',CategoriaRevistaViewSet)
#Visualizacion CRUD de subcategoria
router.register('Registro-de-subcategorias',POSTSubcategoriaRevistaViewSet)
#Visualizacion de datos de subcategori
router.register('Lista-de-subcategorias',SubcategoriaRevistaViewSet)

revista = [
    url('revista/', include(router.urls)),
]