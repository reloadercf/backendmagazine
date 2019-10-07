from .models import Profile, TipoUsuario
from django.contrib.auth.models import User, Permission
from rest_framework import serializers
from revista.serializers import *
from revista.serializers import RevistaSerializer,NomRevistaSerializer
from revista.models import Revista

class TipoSerializer(serializers.ModelSerializer):
	class Meta:
		model	= 	TipoUsuario
		fields 	=	 ['nombre']

class NomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model	= 	User
		fields 	=	 ['username']

class ProfileSerializer(serializers.ModelSerializer):
	revista			=	RevistaSerializer(many=True,read_only=True)
	tipo_usuario	=	TipoSerializer(many=False,read_only=True)
	user 			= 	NomUserSerializer(many=False,read_only=True)
	class Meta:
		model	= 	Profile
		fields 	=	 '__all__'

class POSTProfileSerializer(serializers.ModelSerializer):
	revista			=	serializers.PrimaryKeyRelatedField(
						queryset=Revista.objects.all(),
						required=True,
						many=True)
	tipo_usuario	=	serializers.PrimaryKeyRelatedField(
						queryset=TipoUsuario.objects.all(),
						required=True,
						many=False)
	class Meta:
		model	= 	Profile
		fields 	=	 '__all__'

class ProfileRSerializer(serializers.ModelSerializer):
	revista		=	NomRevistaSerializer(many=True,read_only=True)
	class Meta:
		model = Profile
		fields = ['revista']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename']

class UserSerializer(serializers.ModelSerializer):
	profile_user	=	ProfileSerializer(many=False, read_only=True)
	password 		=	serializers.CharField(write_only=True)
	class Meta:
		model 	= 	User
		fields 	= 	['first_name', 'last_name', 'email', 'id', 'password', 'profile_user']
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.save()
		return user

class POSTUserSerializer(serializers.ModelSerializer):
	password 		=	serializers.CharField(write_only=True)
	class Meta:
		model 	= 	User
		fields 	= 	['username','first_name', 'last_name', 'email', 'id', 'password']
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.save()
		return user

class UserRevistaSerializer(serializers.ModelSerializer):
	profile_user = ProfileRSerializer(many=False, read_only=True)
	class Meta:
		model = User
		fields = ['username','profile_user']

class POSTUserRevistaSerializer(serializers.ModelSerializer):
	revista 	= serializers.PrimaryKeyRelatedField(
					queryset=Revista.objects.all(),
					required=True,
					many=True)
	class Meta:
		model = Profile
		fields = ['user','revista']

class MyUserSerializer(serializers.ModelSerializer):
	profile_user		=	ProfileSerializer(read_only=True)
	user_permissions	=	PermissionSerializer(many=True, read_only=True)
	class Meta:
		model=User
		fields = ['username', 'first_name', 'last_name', 'email','profile_user', 'user_permissions']

		