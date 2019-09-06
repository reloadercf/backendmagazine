from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from rest_framework.authtoken import views
from accounts.urls import accounts

#from articulos.views import *
#from revista.views import *
#from clientes.views import *
#from planrevista.views import *

#articulo=routers.DefaultRouter()

#revista=routers.DefaultRouter()
#cliente=routers.DefaultRouter()
#plan=routers.DefaultRouter()

#articulo.register('registros-de-articulos',ArticuloViewSet)
#articulo.register('registros-de-especiales',EspecialArticuloViewSet)
# cliente.register('registros-de-clientes',ClienteViewSet)
# revista.register('resgistro-de-categoria',CategoriaRevistaViewSet)
# revista.register('registro-de-revista',RevistaViewSet)
# accounts.register('revista-usuario',UserRevistaViewSet)
# plan.register('registro-de-planes',PlanViewSet)
# plan.register('registro-de-formas-de-pago',FormaPagoViewSet)
# plan.register('registro-de-contratos',ContratoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articulo/', include(articulo.urls)),
    # path('accounts/', include(accounts.urls)),
    # path('cliente/', include (cliente.urls)),
    # path('revista/', include (revista.urls)),
    # path('planes/', include(plan.urls)),
    
]+accounts
