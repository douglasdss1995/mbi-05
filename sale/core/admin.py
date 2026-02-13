from django.contrib import admin

from core import models


class BaseModelAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "modified_at", "active"]
    list_filter = ["active"]


class NameBaseModelAdmin(BaseModelAdmin):
    list_display = ["id", "name", "created_at", "modified_at", "active"]
    list_filter = ["name", "active"]


@admin.register(models.Customer)
class FuncionarioAdmin(NameBaseModelAdmin):
    list_display = ["id", "name", "gender"]
    list_filter = ["name", "gender"]

    # Exibir label ao invés do valor
    def get_gender_display(self, obj):
        return obj.get_gender_display()


@admin.register(models.Branch)
class BranchAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.Department)
class DepartmentAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.District)
class DistrictAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.Employee)
class EmployeeAdmin(NameBaseModelAdmin):
    list_display = ["id", "name", "department"]
    list_filter = ["name", "department"]


@admin.register(models.MaritalStatus)
class MaritalStatusAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(NameBaseModelAdmin):
    list_display = [
        "id",
        "name",
        "cost_price",
        "sale_price",
        "product_group",
        "supplier",
    ]
    list_filter = ["name", "cost_price", "sale_price", "product_group", "supplier"]


@admin.register(models.ProductGroup)
class ProductGroupAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.Sale)
class SaleAdmin(BaseModelAdmin):
    list_display = ["id", "customer", "employee", "date"]
    list_filter = ["customer", "employee", "date"]
    date_hierarchy = "date"
    ordering = ["-date"]


@admin.register(models.SaleItem)
class SaleItemAdmin(BaseModelAdmin):
    list_display = ["id", "sale", "product", "quantity", "sale_price"]
    list_filter = ["sale", "product"]


@admin.register(models.State)
class StateAdmin(BaseModelAdmin):
    pass


@admin.register(models.Supplier)
class SupplierAdmin(NameBaseModelAdmin):
    pass


@admin.register(models.Zone)
class ZoneAdmin(NameBaseModelAdmin):
    pass
