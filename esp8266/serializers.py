from .models import Data
from rest_framework import serializers


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('temperature', 'date', 'month', 'humidity')
