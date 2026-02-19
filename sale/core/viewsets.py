from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, serializers, selectors


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(detail=False, methods=['get'])
    def test_queryset(self, request):
        data = selectors.get_all_products()[:5]
        serializer = self.get_serializer(data, many=True)
        return Response(data=serializer.data)
