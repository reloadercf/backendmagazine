from rest_framework import generics
from patrocinadores.pagination import PatrocinadorPagination
#
from revista.serializers import *
from planrevista.serializers import *
from patrocinadores.serializers import *
from articulos.serializers import *
from accounts.serializers import *
from revista.models import *
from planrevista.models import *
from patrocinadores.models import *
from articulos.models import *
from accounts.models import *

class RevistaList(generics.ListAPIView):
    serializer_class    =   RevistaSerializer
    queryset            =   Revista.objects.all()
    def get_queryset(self, *args, **kwargs):
        revista = self.request.GET.get('idrevista')
        plan    = self.request.GET.get('idplan')
        estado  = self.request.GET.get('idestado')
        pais    = self.request.GET.get('idpais')
        queryset_list = super(RevistaList, self).get_queryset()
        if revista:
            queryset_list = queryset_list.filter(id=revista)
        if plan:
            queryset_list = queryset_list.filter(id=plan)
        if estado:
            queryset_list = queryset_list.filter(id=estado)
        if pais:
            queryset_list = queryset_list.filter(id=pais)
        return queryset_list

class CategoriaRevistaList(generics.ListAPIView):
    serializer_class    =   CategoriaSerializer
    queryset            =   Categorias.objects.all()
    def get_queryset(self, *args, **kwargs):
        categoria = self.request.GET.get('idcategoria')
        revista = self.request.GET.get('idrevista')
        queryset_list = super(CategoriaRevistaList, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(id=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista_origen=revista)
        return queryset_list

class PlanList(generics.ListAPIView):
    queryset            =   PlanRevista.objects.all()
    serializer_class    =   PlanSerializer
    def get_queryset(self, *args, **kwargs):
        plan=self.request.GET.get('idplan')
        queryset_list=super(PlanList, self).get_queryset()
        if plan:
            queryset_list=queryset_list.filter(id=plan)
        return queryset_list

class ContratoList(generics.ListAPIView):
    queryset            =   Contrato.objects.all()
    serializer_class    =   ContratoSerializer
    def get_queryset(self, *args, **kwargs):
        contrato = self.request.GET.get('idcontrato')
        revista = self.request.GET.get('idrevista')
        pago = self.request.GET.get('idpago')
        fecha = self.request.GET.get('inicio')
        queryset_list=super(ContratoList, self).get_queryset()
        if contrato:
            queryset_list=queryset_list.filter(id=contrato)
        if revista:
            queryset_list=queryset_list.filter(revista=revista)
        if pago:
            queryset_list=queryset_list.filter(forma_pago=pago)
        if fecha:
            queryset_list=queryset_list.filter(fecha_inicio=fecha)
        return queryset_list

class PatrocinadorList(generics.ListAPIView):
    queryset            =   Patrocinador.objects.all()
    serializer_class    =   PatrocinadorSerializer
    pagination_class    =   PatrocinadorPagination
    def get_queryset(self, *args, **kwargs):
        patrocinador = self.request.GET.get('idpatrocinador')
        revista      = self.request.GET.get('idrevista')
        queryset_list = super(PatrocinadorList, self).get_queryset()
        if patrocinador:
            queryset_list = queryset_list.filter(id=patrocinador)
        if revista:
            queryset_list = queryset_list.filter(revista_pertenencia=revista)
        return queryset_list

class ArticuloList(generics.ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    def get_queryset(self,*args,**kwargs):
        categoria       =       self.request.GET.get("idcategoria")
        subcategoria    =       self.request.GET.get("idsubcategoria")
        origen_revista  =       self.request.GET.get("idrevista")
        titulo          =       self.request.GET.get("slug")
        fin             =       self.request.GET.get("fin")
        queryset_list = super(ArticuloList, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(categoria=subcategoria)
        if origen_revista:
            queryset_list = queryset_list.filter(origen_revista__nombre_revista=origen_revista)
        if fin:
            queryset_list = queryset_list.filter(fecha_fin=fin)
        if titulo:
            queryset_list = queryset_list.filter(slug=titulo)
        return queryset_list

class EspecialArticuloList(generics.ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = EspecialArticulo
    def get_queryset(self,*args,**kwargs):
        categoria       =       self.request.GET.get("idcategoria")
        subcategoria    =       self.request.GET.get("idsubcategoria")
        origen_revista  =       self.request.GET.get("idrevista")
        titulo          =       self.request.GET.get("slug")
        portada         =       self.request.GET.get("portada")
        status          =       self.request.GET.get("status")
        queryset_list = super(EspecialArticuloList, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria=categoria)
        if subcategoria:
            queryset_list = queryset_list.filter(categoria=subcategoria)
        if origen_revista:
            queryset_list = queryset_list.filter(origen_revista__nombre_revista=origen_revista)
        if titulo:
            queryset_list = queryset_list.filter(slug=titulo)
        if portada:
            queryset_list = queryset_list.filter(en_portada=portada)
        if status:
            queryset_list = queryset_list.filter(status=status)
        return queryset_list

class ProfileList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def get_queryset(self, *args, **kwargs):
		user	=	self.request.GET.get('username')
		iduser 	= 	self.request.GET.get('iduser')
		first	=	self.request.GET.get('nombre')
		last	=	self.request.GET.get('apellido')
		revista	=	self.request.GET.get('idrevista')
		tipo	=	self.request.GET.get('idtipo')
		queryset_list = super(ProfileList, self).get_queryset()
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

class UserRevistaList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserRevistaSerializer
	def get_queryset(self, *args, **kwargs):
		revista = self.request.GET.get('idrevista')
		user	= self.request.GET.get('iduser')
		queryset_list = super(UserRevistaList, self).get_queryset()
		if revista:
			queryset_list = queryset_list.filter(profile_user__revista__id=revista)
		if user:
			queryset_list = queryset_list.filter(id=user)
		return queryset_list