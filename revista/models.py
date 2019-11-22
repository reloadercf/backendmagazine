from django.db import models
from regiones.models import Region,Subregion,Ciudad

# Create your models here.
class Categorias(models.Model):
    nombre_categoria    =   models.CharField(max_length=80)
    revista_origen      =   models.ForeignKey("revista.Revista", related_name='cat_revista', on_delete=models.CASCADE)
    icono               =   models.ForeignKey("revista.Icon", related_name='cat_icon', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.nombre_categoria 
    
class Revista(models.Model):
    nombre_revista          =   models.CharField(max_length=100, unique=True)
    logo                    =   models.URLField(max_length=300, blank=True, null=True)
    descripcion             =   models.TextField(blank=True, null=True)
    country                 =   models.ManyToManyField(Region)
    state                   =   models.ManyToManyField(Subregion)
    city                    =   models.ManyToManyField(Ciudad)
    plan                    =   models.ForeignKey('planrevista.PlanRevista', related_name='revista_plan', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_revista

class Subcategorias(models.Model):
    nombre_subcategoria     =   models.CharField(max_length=80)
    categoria               =   models.ForeignKey("revista.Categorias", related_name="categoria_sub", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_subcategoria 

class Icon(models.Model):
    nombre      =   models.CharField(max_length=200)
    relacion    =   models.TextField()
    def __str__(self):
        return self.nombre