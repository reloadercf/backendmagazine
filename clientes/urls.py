from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
router.register('registros-de-clientes',ClienteViewSet)

clientes= [
    path('clientes/', include(router.urls)),
]