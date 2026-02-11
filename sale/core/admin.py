from django.contrib import admin

from core import models

@admin.register(models.ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'commission_percentage',
        'gain_percentage',
    )
    ordering = (
        'id',
        'name',
        'commission_percentage',
        'gain_percentage'
    )
