from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
#vista de permisos
router.register('Lista-de-permisos',PermissionViewSet)
#vista de usuarios con datos de perfil
router.register('Lista-de-usuarios',ProfileViewSet)
#CRUD de usuarios
router.register('Registro-de-usuarios',POSTUserViewSet)
#CRUD de perfiles para usuarios
router.register('Registro-de-perfiles',POSTPerfilesViewSet)
#CRUD de tipo de usuarios
#router.register('Registro-de-tipo_usuarios',TipoViewSet)

accounts = [
    url('accounts/', include(router.urls)),
    url('my_user/', MyUser.as_view()),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
    url('api-auth/', include('rest_framework.urls')),
    #path('api-token-auth/', views.obtain_auth_token),
    url('api-token-auth/', CustomAuthToken.as_view()),
]