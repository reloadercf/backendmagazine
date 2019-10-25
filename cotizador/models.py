from django.db import models
from multiselectfield import MultiSelectField

forma_de_pago =(
    ("Mensual","Mensual"),
    ("Anual","Anual")
)

tecnologias_choice = (
    ('Andorid', "Android"),
    ('IOS', "IOS"),
    ('Web', "Web"),
)


class Cotizador(models.Model):
    no_publicaciones    =   models.IntegerField()
    no_usuarios         =   models.IntegerField()
    tecnologias         =   MultiSelectField (choices = tecnologias_choice)
    otras_funciones     =   models.BooleanField(default=False)
    forma_pago          =   models.CharField(choices=forma_de_pago, max_length=50)
    descuento           =   models.CharField(max_length=50, blank=True, null=True)