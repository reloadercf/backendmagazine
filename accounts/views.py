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

class POSTUserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = POSTUserSerializer
	def get_serializer_class(self):
		serializer_class = self.serializer_class
		if self.request.method == ['PUT', 'PATCH']:
			serializer_class = SerializerWithoutPasswordField
		return serializer_class

class POSTPerfilesViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = POSTProfileSerializer

class TipoViewSet(viewsets.ModelViewSet):
	queryset = TipoUsuario.objects.all()
	serializer_class = TipoSerializer
	def get_queryset(self, *args, **kwargs):
		tipo = self.request.GET.get('idtipo')
		queryset_list = super(TipoViewSet, self).get_queryset()
		if tipo:
			queryset_list = queryset_list.filter(id=tipo)
		return queryset_list

class MyUser(APIView):	
	def get(self, request, format=None):
		my_user = User.objects.all().get(id=request.user.id)
		serializer = MyUserSerializer(my_user)
		return Response(serializer.data)

import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('serviceAccountKey.json')
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
