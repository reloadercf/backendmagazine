from django.db import models
from multiselectfield import MultiSelectField
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string, get_template

forma_de_pago =(
    ("Mensual","Mensual"),
    ("Anual","Anual")
)

tecnologias_choice = (
    ('ANDROID', "ANDROID"),
    ('IOS', "IOS"),
    ('WEB', "WEB"),
)


class Cotizador(models.Model):
    no_publicaciones    =   models.IntegerField()
    no_usuarios         =   models.IntegerField()
    tecnologias         =   MultiSelectField (choices = tecnologias_choice)
    otras_funciones     =   models.BooleanField(default=False)
    forma_pago          =   models.CharField(choices=forma_de_pago, max_length=50)
    descuento           =   models.CharField(max_length=50, blank=True, null=True)
    costo               =   models.DecimalField(decimal_places=4, max_digits=10, blank=True, null=True)
    fecha_creacion      =   models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Cotizador)
def send_cotizacion(sender, instance, *args, **kwargs):
    # send an e-mail to the user
    context = {
        'publicaciones': instance.no_publicaciones,
        'usuarios': instance.no_usuarios,
        'tecnologias' : instance.tecnologias,
        'funciones': instance.otras_funciones,
        'forma': instance.forma_pago,
        'descuento' : instance.descuento,
        'costo' : instance.costo,
        'creacion': instance.fecha_creacion
    }

    # render email text
    mensaje = get_template('cotizacion.html').render(context)
    email_html_message = "Cotizacion"

    msg = EmailMultiAlternatives(
        # title:
        "Cotizacion de {title}".format(title="YouMagazine"),
        # message:
        email_html_message,
        # from:
        "mariovaldez@planb.com.mx",
        # to:
        ["mvaldez7497@gmail.com"]
    )
    msg.attach_alternative(mensaje, "text/html")
    msg.send()