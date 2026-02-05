from django.contrib import admin

from usuarios import models


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ativo',
        'nome',
        'salario',
    )
    ordering = (
        'id',
        'ativo',
        'nome',
        'salario',
    )
