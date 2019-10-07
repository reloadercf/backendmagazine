from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
router.register('Lista-de-categoria',CategoriaRevistaViewSet)
router.register('Lista-de-revista',RevistaViewSet)
router.register('Registro-de-categorias',POSTCategoriaRevistaViewSet)
router.register('Registro-de-revistas',POSTRevistaViewSet)

revista = [
    url('revista/', include(router.urls)),
]