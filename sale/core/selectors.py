from decimal import Decimal

from django.db.models import F, QuerySet

from core import models
from core.models import Employee, Product


def deactivate_all_products() -> int:
    return models.Product.objects.all().update(active=False)


def update_product_comission(group_id: int, new_comission: int) -> int:
    return models.Product.objects.filter(group_id=group_id).update(active=False)


def update_salary_for_all_employees(add_percentage: Decimal) -> int:
    return models.Employee.objects.all().update(
        salary=F(name="salary") * (1 + add_percentage / 100)
    )


def update_product_sale(product_id: int, new_sale: Decimal) -> int:
    return models.Product.objects.filter(id=product_id).update(
        sale_price=new_sale
    )


def update_product_group_gain_percentage(product_id: int, new_gain_percentage: Decimal) -> int:
    return models.ProductGroup.objects.filter(id=product_id).update(
        gain_percentage=new_gain_percentage
    )


def update_salary_departament_ti(departament_id: int, new_salary: Decimal) -> int:
    return models.Employee.objects.filter(id=departament_id).update(
        salary=new_salary
    )


def get_all_employes():
    return models.Employee.objects.all()


def get_all_departments():
    return models.Department.objects.all()


def delete_zone_by_id(zone_id: int) -> tuple:
    return models.Zone.objects.filter(id=zone_id).delete()


def count_all_products() -> int:
    return models.Product.objects.count()


def count_active_employees() -> int:
    return models.Employee.objects.filter(active=True).count()


def count_active_customer() -> int:
    return models.Customer.objects.filter(active=True).count()


def has_customer_with_name(name: str) -> bool:
    return models.Customer.objects.filter(name=name).exists()


def get_first_active_employee() -> Employee | None:
    return models.Employee.objects.filter(active=True).first()


def get_first_five_products() -> QuerySet[Product]:
    return models.Product.objects.all()[:5]


def get_products_from_6_to_10() -> QuerySet[Product]:
    return models.Product.objects.all()[5:10]


def get_high_salary_employees(min_salary: Decimal) -> QuerySet[Employee]:
    return models.Employee.objects.filter(salary__gte=min_salary).all()


def get_products_by_name_contains(term: str) -> QuerySet[Product]:
    return models.Product.objects.filter(name__icontains=term)


def get_employees_name_startswith(prefix: str) -> QuerySet[Employee]:
    return models.Employee.objects.filter(name__istartswith=prefix)


def count_employees_startswith(prefix: str) -> int:
    return models.Employee.objects.filter(name__istartswith=prefix).count()


def count_employees_by_name(name: str) -> int:
    return models.Employee.objects.filter(name__icontains=name).count()
