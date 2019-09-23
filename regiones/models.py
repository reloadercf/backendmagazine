from django.db import models

# Create your models here.
class Region(models.Model):
    nombre_pais        =   models.CharField(max_length=80)
    def __str__(self):
        return self.nombre_pais 
    
class Subregion(models.Model):
    nombre_estado       =   models.CharField(max_length=80)
    pais                =   models.ForeignKey('regiones.Region', related_name='pais_estado', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_estado