from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from .models import Profile
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.db.models import Q
#from youmagazinebackend.settings import key

#vista para visualizacion de permisos
class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Permission.objects.exclude(Q(name__contains="Can"))
	serializer_class = PermissionSerializer

#vista para visualizacion de datos de usuarios
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def get_queryset(self, *args, **kwargs):
		nombre = self.request.GET.get("nombre")
		revista	=	self.request.GET.get('idrevista')
		tipo	=	self.request.GET.get('idtipo')
		queryset_list = super(ProfileViewSet, self).get_queryset()
		if nombre:
			queryset_list = queryset_list.filter(
				Q(first_name__contains=nombre)|
				Q(last_name__contains=nombre)|
				Q(username__contains=nombre)
            )
		if revista:
			queryset_list = queryset_list.filter(profile_user__revista__id=revista)
		if tipo:
			queryset_list = queryset_list.filter(profile_user__tipo_usuario__id=tipo)
		return queryset_list

#vista para CRUD de datos de usuarios
class POSTUserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = POSTUserSerializer
	def get_serializer_class(self):
		serializer_class = self.serializer_class
		if self.request.method == 'PATCH' or self.request.method == 'PUT':
			serializer_class = SerializerWithoutPasswordField
		return serializer_class

#vista para CRUD de datos de perfiles
class POSTPerfilesViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = POSTProfileSerializer

#vista para CRUD de datos de tipo de usuarios
# class TipoViewSet(viewsets.ModelViewSet):
# 	queryset = TipoUsuario.objects.all()
# 	serializer_class = TipoSerializer

#vista para visualizacion de datos de usuario loggeado
class MyUser(APIView):
	def get(self, request, format=None):
		my_user = User.objects.all().get(id=request.user.id)
		serializer = MyUserSerializer(my_user)
		return Response(serializer.data)

#----------- Firebase------------------------------------------------------
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "youmagazine-109a9",
  
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxTjNFEd/y0KVO\nhhHZJR7iHkQb+lkTaEtogX2/c9WU3COJPrfKdGXt4adtZJWa+YehIyKMyEpK4shZ\n+rg2C99xOLp7EHCpEBRSunSTbXcDewjaH8nnBL/W1zEd0QqfkwW9vtHWshcwPln3\nh3I8g5s10VunYU/GVfUpS+p8cPnF9E0tOuLKGwRbumHn+JKSSuqnsbrrBt6TjWvL\nUHM7pgochkCbQR+el0S/rVvMyg1RS85roiGh2ZADEs3gTdiMeudw9Nwi+Mx7GXui\n+FiEVZowKqycCx1nzFyFcvQd7b8sKC7gmBHALIA8xqkiXEHePqMzuaglq4vNctlg\nGdCktst1AgMBAAECggEAIyyFkMX5RMEeDiwcNdT+obKJ5ff9/FLkJM0NjnHTFOcw\nGI3L5bq+Ltklfxblc/tdK/sdo0qnrF/9iZYqvbQQxXQQ0JGkG/Hv6jKJpmagpdze\nVnFYez9OtHb3zDe4cQw4ZxpIJByr63rvG6Mv5y/flmdcVKICMrFCQ8lG8R1ze5DF\nPwRQ7puAJtOBM3qYdr9F3WxeJeFvl3dv9dnsW1mMly41YFBBXxyZ+SLSOn3KJjWR\ntLt5ZwylQ8PrcY+ZFxlKgYlOjWWLgF9XydIArIUOcx2khfq8UkrnKne/F0ejtLXV\nn9COm+qteGbNusOQu5112QuZN6Yo8loPqFmZZwnBSQKBgQDbM9tPs87RtEOiAJWc\n0MAESSCz/EQGxk6NDJf19zG+84KOs11tks8KWVHLWnvwyadmM273NpEfrX6pI5Nq\nbbH6BDnTyMfgBFE/ned6zcoWeihexBSj9ffVvnf8+GAq5AS4HjhTSH0px3Itl/+2\nF1U4S8zSDyR6SYy4YJbnAelDWQKBgQDPEdUgmUPMuuo39iiLaUQKrfku3CRlDsob\nfTpLVkQfRo3Ttr1UetOm3V7etvSUzwuSYC1+ASGIwdAx9a/WsnSZ5sF6v+ZoRiZg\nRsbjqLzKVQlsodBgmsloOadzyVfdMsdPpC4bIZFzLNvlWbrv3qKK7Wj0XfJ5CtKK\nqx+AKBgRfQKBgBNMi4CG6iyYXGQE/ScjUeSOs6xlB3A5QW01sKNdMioHsnTx4cXl\n6QiWOJdYzhSzDGP5H0nwqfJKCh7GHRJ/ue2zNYwp3z8f4i9hraGoQKSd+LPvO4n7\n++f7rwC8tWrRTIERWBAtD6gAAVN2UHMttrkQI2ZTIvkJRLRu/Jo2Ft1xAoGAJ4OF\nohTdJUI907P7hK7vtwH/3PtRTp+F3b0F1L5/fWBfTBlBA8/0d5Eiu2k6PvNLiAEm\nbTcWCRzC9+WkSln/eibYoO3hr+BDDngzF9ppPEsB42L1epnO+T6XP7caNzGrav0v\ndynusYXL6HY4//ECH3SyZH9Q99wi1SdWeYQtI5kCgYEAuFpmkR0I+VkBj/cFhgPZ\n9sIFRJCfninZ8GPICdZqO6qu2nHxohkzQnz9nMxh8yOCjesb/FRQjtC45cgaLgzb\nb1OdfQNs+8HiIprH3POLFic9eAQSVOZG/yBf3HASvEEpdjYuD/9zdGL9+tdATzvw\neJT5WvXuHsbpt91BwWYwTe4=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cuw0l@youmagazine-109a9.iam.gserviceaccount.com",
  "client_id": "100994262960954053826",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cuw0l%40youmagazine-109a9.iam.gserviceaccount.com"
})
default_app = firebase_admin.initialize_app(cred)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        uid= token.key
        custom_token=auth.create_custom_token(uid)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'firebase':custom_token
        })
