from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'productgroup', viewsets.ProductGroupViewSet)
router.register(r'supplier', viewsets.SupplierViewSet)
router.register(r'product', viewsets.ProductViewSet)
router.register(r'departament', viewsets.DepartmentViewSet)
router.register(r'MaritalStatus', viewsets.MaritalStateViewSet)
router.register(r'zone', viewsets.ZoneViewSet)
router.register(r'state', viewsets.StateViewSet)
router.register(r'city', viewsets.CityViewSet)
router.register(r'district', viewsets.DistrictViewSet)
router.register(r'branch', viewsets.BranchViewSet)
router.register(r'employee', viewsets.EmployeeViewSet)
router.register(r'customer', viewsets.CustomerViewSet)
router.register(r'Sale', viewsets.SaleViewSet)
router.register(r'saleItem', viewsets.SaleItemViewSet)

urlpatterns = router.urls
