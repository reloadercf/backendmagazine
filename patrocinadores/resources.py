from import_export import  resources
from import_export.fields import Field
from .models import Patrocinador

class PatrocinadorResource(resources.ModelResource):
    class Meta:
        model=Patrocinador
