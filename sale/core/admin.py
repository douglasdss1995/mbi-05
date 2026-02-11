from django.contrib import admin

from core import models


@admin.register(models.ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    pass
