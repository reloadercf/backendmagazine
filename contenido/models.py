from django.db import models

tipo=(
    ("Imagen","Imagen"),
    ("Texto","Texto"),
    ("Video","Video"),
    ("Publicidad","Publicidad")
)

class Contenido(models.Model):
    articulo    =   models.ForeignKey("articulos.Articulo", related_name='con_art', on_delete=models.CASCADE)
    tipo        =   models.CharField(choices=tipo, max_length=200)
    recurso     =   models.TextField()
    alt       =   models.TextField(blank=True, null=True)
    def __str__(self):
        return self.articulo.titulo