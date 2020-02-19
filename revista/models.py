from django.db import models
from regiones.models import Region,Subregion,Ciudad

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

class Categorias(models.Model):
    nombre_categoria    =   models.CharField(max_length=80)
    revista_origen      =   models.ForeignKey("revista.Revista", related_name='cat_revista', on_delete=models.CASCADE)
    icono               =   models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.nombre_categoria 

class Subcategorias(models.Model):
    nombre_subcategoria     =   models.CharField(max_length=80)
    categoria               =   models.ForeignKey("revista.Categorias", related_name="categoria_sub", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_subcategoria 

