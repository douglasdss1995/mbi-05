from rest_framework import routers

from usuarios import viewsets

router = routers.DefaultRouter()
router.register(r"funcionario", viewsets.FuncionarioViewSet)
router.register(r"departamento", viewsets.DepartamentoViewSet)
router.register(r"vendedor", viewsets.VendedorViewSet)
router.register(r"produto", viewsets.ProdutoViewSet)
router.register(r"venda", viewsets.VendaViewSet)
router.register(r"vendaitem", viewsets.VendaItemViewSet)
router.register(r"cliente", viewsets.ClienteViewSet)

urlpatterns = router.urls
