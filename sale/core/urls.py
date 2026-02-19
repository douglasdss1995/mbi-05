from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()

router.register('product_group', viewsets.ProductGroupViewSet)
router.register('product', viewsets.ProductViewSet)

urlpatterns = router.urls
