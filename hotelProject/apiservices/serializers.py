from rest_framework import serializers
# now import models from models.py
from roomManager.models import Service


# create a models serializer

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'name_ar', 'price', 'description')
