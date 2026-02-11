from rest_framework import serializers

from core import models

class ProductGroupSerializer(serializers.ModelSerializer) :
    class Meta:
          model = models.ProductGroup
          fields = '_all __ '