from django.conf.urls import url
from .views import *

publicos = [
    url(r'revistas/', RevistaList.as_view()),
    url(r'categorias/', CategoriaRevistaList.as_view()),
    url(r'planes/', PlanList.as_view()),
    url(r'contratos/', ContratoList.as_view()),
    url(r'patrocinadores/', PatrocinadorList.as_view()),
    url(r'articulos/', ArticuloList.as_view()),
    url(r'articulos-especiales/', EspecialArticuloList.as_view()),
    url(r'perfiles/', ProfileList.as_view()),
    url(r'usuario-revista/', UserRevistaList.as_view()),
]