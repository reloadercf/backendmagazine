from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from rest_framework.authtoken import views
from accounts.urls import accounts
from revista.urls import revista
from articulos.urls import articulo
from planrevista.urls import planes
from clientes.urls import clientes

urlpatterns = [
    path('admin/', admin.site.urls),    
]+revista+articulo+planes+accounts+clientes
