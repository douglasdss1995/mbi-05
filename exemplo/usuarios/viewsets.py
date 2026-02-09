from rest_framework import viewsets

from usuarios import models, serializers


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = models.Funcionario.objects.all()
    serializer_class = serializers.FuncionarioSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Departamento.objects.all()
    serializer_class = serializers.DepartamentoSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = models.Vendedor.objects.all()
    serializer_class = serializers.VendedorSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = models.Venda.objects.all()
    serializer_class = serializers.VendaSerializer


class VendaItemViewSet(viewsets.ModelViewSet):
    queryset = models.VendaItem.objects.all()
    serializer_class = serializers.VendaItemSerializer
