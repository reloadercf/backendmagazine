from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyUserSerializer, UserRevistaSerializer
from .models import Profile
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def get_queryset(self, *args, **kwargs):
		user	=	self.request.GET.get('username')
		iduser 	= 	self.request.GET.get('iduser')
		first	=	self.request.GET.get('nombre')
		last	=	self.request.GET.get('apellido')
		revista	=	self.request.GET.get('idrevista')
		tipo	=	self.request.GET.get('idtipo')
		queryset_list = super(ProfileViewSet, self).get_queryset()
		if user:
			queryset_list = queryset_list.filter(username=user)
		if iduser:
			queryset_list = queryset_list.filter(id=iduser)
		if first:
			queryset_list = queryset_list.filter(first_name=first)
		if last:
			queryset_list = queryset_list.filter(last_name=last)
		if revista:
			queryset_list = queryset_list.filter(profile_user__revista__id=revista)
		if tipo:
			queryset_list = queryset_list.filter(profile_user__tipo_usuario__id=tipo)
		return queryset_list

class UserRevistaViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserRevistaSerializer
	def get_queryset(self, *args, **kwargs):
		revista = self.request.GET.get('idrevista')
		user	= self.request.GET.get('iduser')
		queryset_list = super(UserRevistaViewSet, self).get_queryset()
		if revista:
			queryset_list = queryset_list.filter(profile_user__revista__id=revista)
		if user:
			queryset_list = queryset_list.filter(id=user)
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
