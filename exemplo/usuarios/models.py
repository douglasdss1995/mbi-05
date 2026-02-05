from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    ativo = models.BooleanField(null=False, blank=False, default=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    departamento = models.ForeignKey(
        to='Departamento',
        on_delete=models.RESTRICT,
        null=True
    )

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    ativo = models.BooleanField(null=False, blank=False, default=True)
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'ID: {self.id} - Descrição: {self.descricao}'
