from django.db import models
from revista.models import Revista
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

#los choices
status_articulo_choice =(
    ("Publicado","Publicado"),
    ("No Publicado","No publicado")
)
video_choice=(
    ("youtube","youtube"),
    ("vimeo","vimeo"),
    ("sin video","sin video")
) 


class Articulo(models.Model):
    titulo                  =   models.CharField(max_length=250)
    en_portada              =   models.BooleanField(default=False)
    origen_revista          =   models.ForeignKey("revista.Revista", related_name='art_revista', on_delete=models.CASCADE)
    categoria               =   models.ForeignKey("revista.Categorias", related_name='art_cat', on_delete=models.CASCADE)
    subcategoria            =   models.ForeignKey("revista.Subcategorias", related_name='art_subcat', on_delete=models.CASCADE)   
    imagen                  =   models.URLField()
    redactado_por           =   models.CharField(max_length=300,null=True,blank=True)
    publicado               =   models.BooleanField(default=False)
    cortesia_de             =   models.CharField(max_length=300,null=True,blank=True)
    fecha_publicacion       =   models.DateField(blank=False,null=False)
    fecha_fin                =   models.DateField(blank=False,null=False)
    fecha_creacion          =   models.DateField(auto_now_add=True)
    fecha_modificacion       =   models.DateField(auto_now=True)
    slug                    =   models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titulo

# Esta funcion genera un SLUG para cada articulo
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Articulo)



# Esta funcion genera un SLUG para cada articulo
def pre_save_articulo(sender, instance, *args, **kwargs):
    if not instance.titulo:
        instance.titulo = '%s' % (instance.articulo.titulo)


pre_save.connect(pre_save_articulo, sender=Articulo)
