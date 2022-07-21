from rest_framework import serializers
# now import models from models.py
from roomManager.models import Service
from currencyapp.models import Currency


# create a models serializer


# class currencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Currency
#         fields = ('name', 'symbole')
#
#
# class ServicesSerializer(serializers.ModelSerializer):
#     currency = currencySerializer(many=True)
#
#     class Meta:
#         model = Service
#         fields = ('name', 'name_ar', 'price', 'currency', 'description')

class ServicesSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    # name_ar = serializers.CharField(required=False, allow_blank=True, max_length=50)
    # price = serializers.DecimalField(required=True, max_digits=10, decimal_places=3)
    # # currency = serializers.ListField(*args, **kwargs)
    # description = serializers.CharField(required=False, allow_blank=True, max_length=250)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Service.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.name_ar = validated_data.get('name_ar', instance.name_ar)
    #     instance.price = validated_data.get('price', instance.price)
    #     # instance.currency = validated_data.get('currency', instance.currency)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance

    class Meta:
        model = Service
        fields = ('name', 'name_ar', 'price', 'currency', 'description')
