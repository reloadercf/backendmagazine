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
  "private_key_id": "027692cca7a48c0d365124f0c63612fc62720559",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCpKrATDGjSKPZ+\nTK58vFs0nbTc5Np5l5wkAyIxcrdCH0nVhWOI5fRTr1XAjmPfzZjni+M6MpHTzLOA\nFp4pX3rX1AsHqH6geruErsvgaLXjmU0fIZQY1LJQRmnaG+mx9Z2rAFxLPxUw6kmV\nJa+ybJjllA9TiGgFZyGhKX3SrbWzzaocl8eXQ9Ga5hmZKZsQbMnCjQRd90+RSsRC\ncrLW665AXoeyIF5JTePEhF/LhcMLP2qtKjyMLu3XPDnGDfaJTRJnYo/6GJkUmYVL\nfwys7CuTuFN4fbwEmSkXbg/yLVim7ckn0bkjzULOKtTg0IPYmzt8zqaO2Qk0mAo6\ni6Q0QIahAgMBAAECggEABV0DbDYu8ldOwdg46b7fyiQ0IFL/534eWuCvzkcpnt6+\ntLaj/kqSn47Z+lb1XQqP3gr4CT/CUneNaxqkePG0U4iPMTbnDVvYy0MOtxKgziqN\niLa0AyHGtb92wo3TH+OWdC4IrxDM4WIzMyeoyXCSnChAoGSNLjsr5Hf8G5Bq9+xo\nlIukmFN/PhSiKtk3BYClnKKLMFAVOw/GH8vPfMQ4kXgnlAYlEalP3CRN31ayf9ep\ndqW469QCrTF9HB90j09iH/zKbWYNFpbesiYMEDUduzHThh4s7NKXKlssOD2eu0ED\neByjTEAHMh7a3kKERTnnVFjxwIBR79TVp//lQ66jEQKBgQDVumBDvv9VY2y9yZFv\n3muoLi7SMxeoWYylFOuNzD9/ClvFDvQYYiUKa8NMPp7v5PCrV8YwP6vn0OIuELE/\nB/J13BkDfe+0UzyDbgBtH+7/vLfercbLetVKmo+YtAoo4GfzbvJkV12yqUvR/WbP\nVvvIXO5Jpssszq2epWQTqSD98QKBgQDKoA3uUH2FeID9b9ywBBTgVnnctezG6vwE\nkm8zM3GU4wTnIXaCSFp1yUCX5SPFNveAqwUATZkpYBhS7GeDbPCCBkAEugMWERsu\nDECZ5egSbcDU5lmTGA0h2YxFH63SCd8EPYGi2Sm0NbafwSsBMhBckeS1h4k8nIY7\nVkBR2EkjsQKBgCtReh9g/9lrrGePCiY1W3ab3auG5X2eoM34voFf62KxU8ZN8JVc\nlwtUqiGy833F1i20PZwb25jBkoYppfMThkXzFTLK/KF82V/+FKIJfeRheJbue8NU\nIxTa3M3jd8evLAJ/8yr5Nil2/MIT7RmLFL8YbseIwddUEIZ+GRmPBvvRAoGAVKyc\nBbn3Kl6YMNCdPaUHAFTC6hvQTbQHCvYSqCfYUCqqctgGCR2pR82JQ7CKyTBWL5vI\nJD9JQQQaRhTqkP5mZz+rYw5EmeUeIZkXKfjsiT76NT3pstF7M2kQ+BXr8nkTjFcT\npHTxu5AyuAHmMcK1GaoSFFYGYKDca1F44Xrr3ZECgYEAj2qFw+KS0SOZbGrS+GVg\nVfBHBTuzubKeIl89Tg8s5DMYEFZHLJhaoXlS2CRo04l1k/i0X7ypwCcf5d6DAmrI\nsVEajjEAjz9yrdx4gbdfgHsp6tTlLLBQgrfkcbQB4x497ZOacvDYtvsvSO/IPwiS\nn0RvR4Aw2NrXw3u1EzVNdB4=\n-----END PRIVATE KEY-----\n",
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
