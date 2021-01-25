from . import models
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

