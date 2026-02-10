from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'product_group', viewsets.ProductGroupViewSet)

urlpatterns = router.urls