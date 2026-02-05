from rest_framework import routers

from usuarios import viewsets

router = routers.DefaultRouter()
router.register(r'funcionario', viewsets.FuncionarioViewSet)
router.register(r'departamento', viewsets.DepartamentoViewSet)

urlpatterns = router.urls
