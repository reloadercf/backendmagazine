from django.db import models

llamadas=(
    ("Contactar","Contactar"),
    ("Visitar","Visitar"),
    ("Compar","Comprar"),
    ("Llamar","Llamar"),
    ("Sin llamada","Sin llamada")
)

class Publicidad(models.Model):
    nombre          =   models.CharField(max_length=200)
    recurso         =   models.TextField()
    texto           =   models.TextField(blank=True,null=True)
    accion          =   models.CharField(choices=llamadas, max_length=200)
    patrocinador    =   models.ForeignKey("patrocinadores.Patrocinador", related_name='pub_pat', on_delete=models.CASCADE
)
    def __str__(self):
        return self.nombre