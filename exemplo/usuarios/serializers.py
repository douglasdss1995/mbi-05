from rest_framework import serializers

from usuarios import models


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Funcionario
        fields = "__all__"


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departamento
        fields = "__all__"


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendedor
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = "__all__"


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venda
        fields = "__all__"


class VendaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VendaItem
        fields = "__all__"
