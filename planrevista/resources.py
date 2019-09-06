from import_export import  resources
from import_export.fields import Field
from .models import PlanRevista

class PlanResource(resources.ModelResource):
    class Meta:
        model=PlanRevista