from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from core import models, serializers

class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer