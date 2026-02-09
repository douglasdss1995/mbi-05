from django.db import models


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"ID: {self.id} - Ativo: {self.ativo}"


class Funcionario(ModeloBase):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    salario = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    departamento = models.ForeignKey(
        to="Departamento", on_delete=models.RESTRICT, null=True
    )

    def __str__(self):
        return self.nome


class Departamento(ModeloBase):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"ID: {self.id} - Descrição: {self.descricao}"


class Vendedor(ModeloBase):
    nome = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome


class Produto(ModeloBase):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.descricao


class Venda(ModeloBase):
    vendedor = models.ForeignKey(to="Vendedor", on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return f"ID: {self.id}"


class VendaItem(ModeloBase):
    venda = models.ForeignKey(to="Venda", on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey(to="Produto", on_delete=models.RESTRICT, null=True)
    quantidade = models.IntegerField(null=False, blank=False)
    valor_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )

    def __str__(self):
        return f"ID: {self.id} - Venda ID: {self.venda.id} - Produto: {self.produto.descricao} - Quantidade: {self.quantidade}"
