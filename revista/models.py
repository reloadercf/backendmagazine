from django.db import models
from planrevista.models import PlanRevista

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
    plan                    =   models.ForeignKey('planrevista.PlanRevista', related_name='revista_plan', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_revista
