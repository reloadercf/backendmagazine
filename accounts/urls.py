from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
router.register('Lista-de-perfiles',ProfileViewSet)
router.register('Lista-de-usuarios_revistas',UserRevistaViewSet)
router.register('Registro-de-perfiles',POSTPerfilesViewSet)
router.register('Resgistro-de-usuarios_revistas',POSTUserRevistaViewSet)
router.register('Resgistro-de-usuario',POSTProfileViewSet)

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