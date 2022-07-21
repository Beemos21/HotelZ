from rest_framework import serializers
# now import models from models.py
from roomManager.models import Service
from currencyapp.models import Currency


# create a models serializer


class currencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('name', 'symbole')


class ServicesSerializer(serializers.ModelSerializer):
    currency = currencySerializer(many=True)

    class Meta:
        model = Service
        fields = ('name', 'name_ar', 'price', 'currency', 'description')
