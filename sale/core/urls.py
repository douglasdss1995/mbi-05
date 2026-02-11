from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'ProductGroup', viewsets.ProductGroupViewSet)
router.register(r'Supplier', viewsets.SupplierViewSet)
router.register(r'Product', viewsets.ProductViewSet)
router.register(r'SaleItem', viewsets.SaleItemViewSet)
router.register(r'State', viewsets.StateViewSet)
router.register(r'City', viewsets.CityViewSet)
router.register(r'Zone', viewsets.ZoneViewSet)
router.register(r'District', viewsets.DistrictViewSet)
router.register(r'Branch', viewsets.BranchViewSet)
router.register(r'MaritalStatus', viewsets.MaritalStatusViewSet)
router.register(r'Department', viewsets.DepartmentViewSet)
router.register(r'Employee', viewsets.EmployeeViewSet)
router.register(r'Customer', viewsets.CustomerViewSet)
router.register(r'Sale', viewsets.SaleViewSet)

urlpatterns = router.urls
