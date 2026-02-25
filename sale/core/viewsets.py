from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, selectors, serializers, request_serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(detail=False, methods=["get"])
    def test_queryset(self, request):
        data = selectors.get_all_products()[:5]
        serializer = self.get_serializer(data, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=["get"])
    def get_all_employees(self, request):
        data = selectors.get_all_employees()[:5]
        serializer = serializers.EmployeeSerializer(data, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=["get"])
    def count_products(self, request):
        data = selectors.count_all_products()
        return Response(data=data)

    @action(detail=False, methods=["get"])
    def get_products_with_absolute_profit(self, request):
        data = selectors.get_products_with_absolute_profit()
        return Response(data=data)

    @action(detail=False, methods=["get"])
    def spanning_fields(self, request):
        data = models.Product.objects.values("id", "name", "product_group__name")
        return Response(data=data)


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    @action(detail=False, methods=["get"])
    def departments_report(self, request, *args, **kwargs):
        request_serializer = request_serializers.DepartmentPaginatorSerializer(
            data=request.query_params
        )
        request_serializer.is_valid(raise_exception=True)

        queryset = models.Department.objects.values(
            "name"
        ).annotate(
            qtd_employees=Count("employees")
        )[:request_serializer.data["qtd_departments"]]

        return Response(queryset)


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.SaleItem.objects.all()
    serializer_class = serializers.SaleItemSerializer
