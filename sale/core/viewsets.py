from crypt import methods

from django.contrib.admin import action
from django.db.models import Count
from psycopg.rows import args_row
from rest_framework import viewsets
from rest_framework.response import Response

from core import models, serializers


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


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

    @action(detaol=False, methods=["get"])
    def departments_report(self, request *args, **kwargs):
    queryset = models.Department.objects.values(
        "name"
    ).annotate(
        qtd_emloyess=Count("employees"),
    )
    return Response(queryset)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


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
