from rest_framework import serializers
from .models import public

class publicerializer(serializers.ModelSerializer):
    class Meta:
        model = public
        fields = ('title', 'url', 'description', 'style')