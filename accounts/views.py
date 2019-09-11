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
		profile = self.request.GET.get('iduser')
		revista = self.request.GET.get('idrevista')
		queryset_list = super(ProfileViewSet, self).get_queryset()
		if profile:
			queryset_list = queryset_list.filter(id=profile)
		if revista:
			queryset_list = queryset_list.filter(id=revista)
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
