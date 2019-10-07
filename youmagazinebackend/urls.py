from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from rest_framework.authtoken import views
from accounts.urls import accounts
from revista.urls import revista
from articulos.urls import articulo
from planrevista.urls import planes
from patrocinadores.urls import patrocinadores
from publicos.urls import publicos
from regiones.urls import regiones

urlpatterns = [
    url('admin/', admin.site.urls),
    url('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]+accounts+articulo+patrocinadores+planes+regiones+revista+publicos

