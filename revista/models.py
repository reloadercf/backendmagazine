from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre_categoria        =   models.CharField(max_length=80)
    revista_origen          =   models.ForeignKey("revista.Revista", related_name="cat_revista", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_categoria 
    
class Revista(models.Model):
    nombre_revista          =   models.CharField(max_length=80)
    logo                    =   models.URLField(max_length=200, blank=True, null=True)
    descripcion             =   models.TextField(blank=True, null=True)
    country                 =   models.ForeignKey('regiones.Region', related_name='revista_pais', on_delete=models.CASCADE)
    state                   =   models.ForeignKey('regiones.Subregion', related_name='revista_estado', on_delete=models.CASCADE)
    city                    =   models.ForeignKey('regiones.Ciudad', related_name='revista_ciudad', on_delete=models.CASCADE)
    plan                    =   models.ForeignKey('planrevista.PlanRevista', related_name='revista_plan', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_revista

class Subcategorias(models.Model):
    nombre_subcategoria     =   models.CharField(max_length=80)
    categoria               =   models.ForeignKey("revista.Categorias", related_name="categoria_sub", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_subcategoria 
