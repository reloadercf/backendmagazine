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
from youmagazinebackend.settings import key

#vista para visualizacion de permisos
class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Permission.objects.exclude(Q(name__contains="Can"))
	serializer_class = PermissionCSerializer

#vista para visualizacion de datos de usuarios
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()#[:1]#lo que esta entre corchetes es la cantidad de objetos que se mostraran
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
class TipoViewSet(viewsets.ModelViewSet):
	queryset = TipoUsuario.objects.all()
	serializer_class = TipoSerializer

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
  "private_key_id":key,
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDcU0kW7AA2xwi7\nrVj3mMCXmD5g1LGTmG2IkhNWEUMQBZj3jqRfoNO1Y6aGk2ET2DKdrJNVPA73dOSG\nuBcY8fN+8DwO4LQMmi/Yx73G2nX4bL9mdPhVO37hQWnoHk2aPpXoFaCQJHOJfL+a\ned4e1mG9Eqs+3K8mLu8MpO9uP3RML+4a6j2PcxN5h4XSfIHPpx2RyrHCqGbEIROY\n4bJPxUDUy0eWto2VW5hpMvCXK1U5lhdXsbwT5Mu4xOQy21Jl58wJ526s0RSsHBKd\nJfFaizlh8MOxXcoQodRVYMYGrs+JxbM5QCzSReNjAG4TiCFSDCr29BvDaK+dDq0O\n9leHl85RAgMBAAECggEAIkP/s4VruRk2Vf3tPsCuf0UpumSJ45MKwfk58aJIpEbC\nlgnEray1EFpZrUdhizUOFjCfT1vCViEDY6Jg0Tvb60uQg53V0rnuJBBYhwM14reD\nAvvBHXxdzMmgH34LAqimJsyqRpCsuV7B69P1RCWCWOX85Q9sXAtjmTtTk3lh7HEj\n/TZ6d9Ro1Xr6zlVpZrqNdSybip6xSis7rqL5aVm9CNfmZ6bxIxysyMw58rqrPGhZ\nlPjfoCmwD7rYAbfcpJx8V1vxBSq8RH1Mc4ILZsTrlF0xArCkxX0n+/JIDt/r9vbn\nm4na0SQAzUDcfNzdSWTJ//0z7u+jHWQodXuv4MYcuQKBgQDwzAkjM6Gm+Ru+KK+h\n1Y9oUQxsr2nbnTeoRAqALiPh+3XuI5uV4y3wdF88CCXtk3DWXIgDrv0O5wgfisvD\nLj/k9yFkkIs0dg+7NIwRYjZt8etnrfiwOYmLw+wl9WAoINI9guP/EM1C1GiIW9JN\nbzY8tI/ej2+bB6K+gZgUNWERBQKBgQDqPF6HvvGExFc6OW+mKvIEGbkdkuFp8Fuw\nyCWFO9Xt/5mcHr4q2Cv50wUXOuC8U8+7fchQ5pLp2vHopZpICbO1ZZNbf20vT1bA\nJjffXzaCCj32brn4eDgU5qTi8u3owN/noTNK7b5aH7Zh+dVLfzjBF8a8Q5GMg6hK\nYx5bhZo53QKBgQDqiFB+ENPqJcd3t3kZT0CWghpv4YphdQe4xEzV/BrHCH0crWHk\n45jjEvWPKwCGHY1RvF5d+BpSYYPv9Ofx+yIQiQPlR0POnQ9FbzDd3aLWA0MdgL0w\nJ1po3zMq5Yv6ib08XDhlPqAt72TBK23yLdfN2LAoPdyeSxmgI+lUBYm9YQKBgGw1\nn2YOq/ytx646Qn39cPi7+WzUIhaS14j/rXWzgs0EO66H9UpNu2MaPUvSA2h9P4Za\nQWQ+YLhwUTks5+1HriGq3zxxzbsBaA40mbMzhTbmDGIAHSHQR/g/5QSDPa09DTMw\noUWIN1vjMppolETgbROnLERk4qSLXf+fcrLNMcZxAoGBAJQttB7P/iGPWlFXyB5l\nqrLwJU1qC2nXLvBF0KdTXrImghR6LeaYLZdYrMGGQcL5fvsqSX3n5YVmhON4bs17\niJ+YlUyJDvobWc4UvAviaJCJmsfB/+1RC4s+V0OKhIIqQluPyJb/xVXnHdbhQR4e\nX+tdwr9jMYaAbRoToZKnLnoS\n-----END PRIVATE KEY-----\n",
  "client_email": "youmagazine-109a9@appspot.gserviceaccount.com",
  "client_id": "107047606938047887476",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/youmagazine-109a9%40appspot.gserviceaccount.com"
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
