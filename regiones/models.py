from django.db import models

# Create your models here.
class Region(models.Model):
    nombre_region        =   models.CharField(max_length=80)
    def __str__(self):
        return self.nombre_region 
    
class Subregion(models.Model):
    nombre_estado       =   models.CharField(max_length=80)
    def __str__(self):
        return self.nombre_estado