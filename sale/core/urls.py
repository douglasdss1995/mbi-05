from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'product_group', viewsets.ProductGroupViewSet)
router.register(r'supplier', viewsets.SupplierViewSet)
router.register(r'product', viewsets.ProductViewSet)
router.register(r'zone', viewsets.ZoneViewSet)
router.register(r'state', viewsets.StateViewSet)
router.register(r'city', viewsets.CityViewSet)
router.register(r'branch', viewsets.BranchViewSet)
router.register(r'department', viewsets.DepartmentViewSet)
router.register(r'marital_status', viewsets.MaritalStatusViewSet)
router.register(r'employee', viewsets.EmployeeViewSet)
router.register(r'customer', viewsets.CustomerViewSet)
router.register(r'sale', viewsets.SaleViewSet)
router.register(r'sale_item', viewsets.SaleItemViewSet)

urlpatterns = router.urls
