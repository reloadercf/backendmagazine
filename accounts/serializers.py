from .models import Profile
from django.contrib.auth.models import User, Permission
from rest_framework import serializers
from revista.serializers import SoloRevistaSerializer, NomRevistaSerializer

class ProfileSerializer(serializers.ModelSerializer):
	revista=SoloRevistaSerializer(many=False,read_only=True)
	class Meta:
		model = Profile
		fields = ['revista']

class ProfileRSerializer(serializers.ModelSerializer):
	revista=NomRevistaSerializer(many=False,read_only=True)
	class Meta:
		model = Profile
		fields = ['revista']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename']

class UserSerializer(serializers.ModelSerializer):
	profile_user = ProfileSerializer(many=False, read_only=True)
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'id', 'password', 'profile_user']
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

class MyUserSerializer(serializers.ModelSerializer):
	profile_user = ProfileSerializer(read_only=True)
	user_permissions = PermissionSerializer(many=True, read_only=True)
	class Meta:
		model=User
		fields = ['username', 'first_name', 'last_name', 'email','profile_user', 'user_permissions']