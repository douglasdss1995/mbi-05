from rest_framework import serializers

from core import models


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
