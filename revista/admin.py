from django.contrib import admin
from .models import Categorias, Revista, Subcategorias,Icon

# Register your models here.

admin.site.register(Categorias)
admin.site.register(Revista)
admin.site.register(Subcategorias)
admin.site.register(Icon)