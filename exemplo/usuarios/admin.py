from django.contrib import admin

from usuarios import models


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ativo",
        "nome",
        "salario",
    )
    ordering = (
        "id",
        "ativo",
        "nome",
        "salario",
    )


@admin.register(models.Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ativo",
        "descricao",
    )
    ordering = (
        "id",
        "ativo",
        "descricao",
    )


@admin.register(models.Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ativo",
        "nome",
    )
    ordering = (
        "id",
        "ativo",
        "nome",
    )


@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ativo",
        "descricao",
    )
    ordering = (
        "id",
        "ativo",
        "descricao",
    )


@admin.register(models.Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ativo",
        "vendedor",
    )
    ordering = (
        "id",
        "ativo",
        "vendedor",
    )


@admin.register(models.VendaItem)
class VendaItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ativo",
        "venda",
        "produto",
        "quantidade",
        "valor_unitario",
    )
    ordering = (
        "id",
        "ativo",
        "venda",
        "produto",
        "quantidade",
        "valor_unitario",
    )
