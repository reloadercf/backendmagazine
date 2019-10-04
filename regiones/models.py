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

class Ciudad(models.Model):
    nombre_ciudad       =   models.CharField(max_length=80)
    estado              =   models.ForeignKey('regiones.Subregion', related_name='estado_ciudad', on_delete=models.CASCADE)
    def __str__(self):
<<<<<<< HEAD
        return self.nombre_ciudad
=======
        return self.nombre_cuidad
>>>>>>> 6af3e7659c1219a98b3957eca43a2ef525f2e8f6
