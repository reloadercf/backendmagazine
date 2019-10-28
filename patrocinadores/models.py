from django.db import models
from revista.models import Revista
from planrevista.models import PlanRevista

# Create your models here.
class Patrocinador(models.Model):
    nombre              =models.CharField(max_length=100)
    activo              =models.BooleanField()
    razonsocial         =models.CharField(max_length=200)
    correo              =models.EmailField(null=True,blank=True)
    telefono            =models.IntegerField(null=True,blank=True)
    revista_pertenencia =models.ForeignKey('revista.Revista', related_name='pat_revista', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre  