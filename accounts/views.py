from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyUserSerializer, UserRevistaSerializer
from .models import Profile
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def get_queryset(self, *args, **kwargs):
		profile = self.request.GET.get('iduser')
		queryset_list = super(ProfileViewSet, self).get_queryset()
		if profile:
			queryset_list = queryset_list.filter(id=profile)
			return queryset_list

class UserRevistaViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserRevistaSerializer
	def get_queryset(self, *args, **kwargs):
		revista = self.request.GET.get('idrevista')
		queryset_list = super(UserRevistaViewSet, self).get_queryset()
		if revista:
			queryset_list = queryset_list.filter(id=revista)
			return queryset_list

class MyUser(APIView):	
	def get(self, request, format=None):
		my_user = User.objects.all().get(id=request.user.id)
		serializer = MyUserSerializer(my_user)
		return Response(serializer.data)