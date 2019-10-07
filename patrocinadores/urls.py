from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
router.register('Lista-de-Patrocinadores',PatrocinadorViewSet)
router.register('Registro-de-Patrocinadores',POSTPatrocinadorViewSet)

patrocinadores= [
    url('patrocinadores/', include(router.urls)),
]