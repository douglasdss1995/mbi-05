from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register('productgroups', viewsets.ProductGroupViewSet)
router.register('product', viewsets.ProductViewSet)
router.register('customer', viewsets.CustomerViewSet)
router.register('marital_status', viewsets.MaritalStatusViewSet)
router.register('sale', viewsets.SaleViewSet)
router.register('department', viewsets.DepartmentViewSet)
router.register('employee', viewsets.EmployeeViewSet)
router.register('branch', viewsets.BranchViewSet)
router.register('sale_item', viewsets.SaleItemViewSet)
router.register('zone', viewsets.ZoneViewSet)
router.register('supplier', viewsets.SupplierViewSet)
router.register('district', viewsets.DistrictViewSet)
router.register('city', viewsets.CityViewSet)
router.register('state', viewsets.StateViewSet)

urlpatterns = router.urls