from rest_framework import viewsets

from core import models, serializers


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializers = serializers.StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializers = serializers.CitySerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializers = serializers.ZoneSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializers = serializers.DistrictSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializers = serializers.DepartmentSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializers = serializers.BranchSerializer


class MaritalStateViewSet(viewsets.ModelViewSet):
    queryset = models.MaritalStatus.objects.all()
    serializers = serializers.MaritalStatusSerializer


class CustumerViewSet(viewsets.ModelViewSet):
    queryset = models.Custumer.objects.all()
    serializers = serializers.CustomerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializers = serializers.EmployeeSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializers = serializers.SupplierSerializer


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializers = serializers.ProductGroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializers = serializers.ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializers = serializers.SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.SaleItem.objects.all()
    serializers = serializers.SaleItemSerializer
