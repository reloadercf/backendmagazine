from django.db import models
from revista.models import Revista
from planrevista.models import PlanRevista

# Create your models here.
class Cliente(models.Model):
    nombre              =models.CharField(max_length=100)
    activo              =models.BooleanField()
    razonsocial         =models.CharField(max_length=200)
    correo              =models.EmailField(null=True,blank=True)
    telefono            =models.IntegerField(null=True,blank=True)
    numero_cuenta       =models.IntegerField(null=True,blank=True)
    revista_pertenencia =models.ForeignKey('revista.Revista', related_name='revista_origen', on_delete=models.CASCADE)
    iniciocontrato      =models.DateField()
    terminocontrato     =models.DateField()
    fecha_registro      =models.DateTimeField(auto_now_add=True)
    fecha_modificacion  =models.DateTimeField(auto_now=True)
    plan_contratado     =models.ForeignKey("planrevista.PlanRevista", related_name='plan_cliente', on_delete=models.CASCADE)
    contrato            =models.FileField(upload_to='contratos',blank=True,null=True)
    def __str__(self):
        return self.nombre  