from rest_framework import serializers
from .models import Pizzaria

class PizzariaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Pizzaria
        fields='__all__'