from decimal import Decimal

from django.db import transaction
from django.db.models import F, DecimalField, ExpressionWrapper
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, serializers, selectors


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    @action(detail=False, methods=["patch"])
    def increase_salary(self, request):

        percentage = request.data.get("percentage")

        if percentage is None:
            return Response(
                {"error": "percentage is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            percentage = Decimal(str(percentage))
        except:
            return Response(
                {"error": "percentage must be a number"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if percentage <= 0:
            return Response(
                {"error": "percentage must be greater than 0"},
                status=status.HTTP_400_BAD_REQUEST
            )

        increase_factor = Decimal("1") + (percentage / Decimal("100"))

        with transaction.atomic():
            self.get_queryset().update(
                salary=ExpressionWrapper(
                    F('salary') * increase_factor,
                    output_field=DecimalField(max_digits=10, decimal_places=2)
                )
            )

        return Response({
            "message": f"All salaries increased by {percentage}%"
        })


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.SaleItem.objects.all()
    serializer_class = serializers.SaleItemSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(detail=False, methods=['get'])
    def test_queryset(self, request):
        data = selectors.get_all_products()[:5]
        serializer = self.get_serializer(data, many=True)
        return Response(data=serializer.data)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
