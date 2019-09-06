from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .views import *

router = routers.DefaultRouter()
router.register('registro-perfiles',ProfileViewSet)

accounts = [
    path('apis/', include(router.urls)),
    path('my_user/', MyUser.as_view()),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
    path('api-auth/', include('rest_framework.urls')),
    #path('api-token-auth/', views.obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view()),
]