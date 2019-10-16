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
	user_permissions= PermissionSerializer(many=True)
	profile_user	=	ProfileSerializer(many=False)
	class Meta:
		model 	= 	User
		fields 	= 	['id','first_name', 'last_name', 'email', 'id', 'profile_user','user_permissions']


class POSTUserSerializer(serializers.ModelSerializer):
	profile_user	=	ProfileSerializer(many=False, read_only=True)
	password 		=	serializers.CharField(write_only=True)
	class Meta:
		model 	= 	User
		fields 	= 	['id','username','first_name', 'last_name', 'email', 'password', 'profile_user','user_permissions']
	def create(self, validated_data):
		password = validated_data.pop('password')
		user_permissions = validated_data.pop('user_permissions')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.user_permissions.set(user_permissions)
		user.save()
		return user

class SerializerWithoutPasswordField(serializers.ModelSerializer):
    profile_user = ProfileSerializer(read_only=True)
    class Meta:
        model=User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'user_permissions', 'is_active','profile_user']

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)





class UserRevistaSerializer(serializers.ModelSerializer):
	profile_user = ProfileRSerializer(many=False, read_only=True)
	class Meta:
		model = User
		fields = ['username','profile_user']

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class MyUserSerializer(serializers.ModelSerializer):
	profile_user		=	ProfileSerializer(read_only=True)
	user_permissions	=	PermissionSerializer(many=True, read_only=True)
	class Meta:
		model=User
		fields = ['username', 'first_name', 'last_name', 'email','profile_user', 'user_permissions']

		