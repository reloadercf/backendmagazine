from django.db import models
from revista.models import Revista

class PlanRevista(models.Model):
    nombre                      =   models.CharField(max_length=100)
    no_usuarios                 =   models.CharField(max_length=5)
    no_patrocinadores           =   models.CharField(max_length=5)
    no_publicaciones_mensual    =   models.CharField(max_length=5)
    def __str__(self):
        return self.nombre

class Forma_Pago(models.Model):
    nombre      =   models.CharField(max_length=50)
    no_meses    =   models.CharField(max_length=5)
    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    revista         =   models.ForeignKey("revista.Revista", related_name='revista_contrato', on_delete=models.CASCADE)
    forma_pago      =   models.ForeignKey("Forma_Pago", related_name='pago_contrato', on_delete=models.CASCADE)
    fecha_inicio    =   models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.revista.nombre_revista 