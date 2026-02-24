from decimal import Decimal
from typing import Any

from django.db.models import F, QuerySet, Q, Sum, Count

from core import models
from core.models import Employee, Product, Customer, Department, Branch


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


def get_products_by_ids(product_ids: list[int]) -> QuerySet[Product]:
    return models.Product.objects.filter(id__in=product_ids)


def get_all_products():
    return models.Product.objects.all()


def get_products_by_supplier_name(supplier_name: str) -> QuerySet[Product]:
    return models.Product.objects.filter(supplier__name__icontains=supplier_name)


def get_all_suppliers():
    return models.Supplier.objects.all()


def get_products_by_name_or_id(term: str) -> QuerySet[Product]:
    return models.Product.objects.filter(
        Q(name__icontains=term) | Q(id=term)
    )


def get_customer_by_filters(
        name: str,
        city: str = None
) -> QuerySet[Customer]:
    query = Q(name__icontains=name)

    if city:
        query &= Q(district_city__name__icontains=city)
        query &= ~Q(district_id=1)

    return models.Customer.objects.filter(query)


def get_all_customers():
    return models.Customer.objects.all()


def get_all_cities():
    return models.City.objects.all()


def increase_all_salaries(percentage: Decimal) -> int:
    multiplier = 1 + percentage / 100
    return models.Employee.objects.all().update(salary=F(name='salary') * multiplier)


def get_total_salary_with_alias() -> dict:
    return models.Employee.objects.aggregate(total=Sum('salary'))


def get_branch_sales(branch_id: int) -> Decimal:
    return models.Branch.objects.filter(id=branch_id).aggregate(
        total_sale=Sum(
            F(name="sales__sale_items__quantity") * F(name="sales__sale_items__sale_price")
        )
    )["total_sale"] or Decimal(value="0.00")


def get_departments_with_employee_count() -> QuerySet[Department]:
    return models.Department.objects.annotate(
        total_employees=Count('employee')
    )


def get_product_id_and_name() -> QuerySet[Product, dict[str, Any]]:
    return models.Product.objects.values("id", "name")


def get_supplier_name_and_product_group_id():
    return models.Product.objects.values(
        product_id=F(name="id"),
        product_name=F(name="name"),
        group_name=F(name="product_group__name"),
        supplier_name=F(name="supplier__name"),
        price=F(name="sale_price"),
    )


def get_product_count_by_group() -> QuerySet[Product, dict[str, Any]]:
    return models.Product.objects.values("product_group__name").annotate(
        total_poducts=Count("id")
    )


def sale_by_branch(field_name: str = "Total de vendas desta filial:") -> QuerySet[Branch, dict[str, Any]]:
    return models.Branch.objects.values("name").annotate(**{field_name: Sum('sales')})


def product_group_count() -> None:
    result = (
        Product.objects.filter(product_group__active=True)
        .values(product_group_name=F("product_group__name"))
        .annotate(total=Count("id"))
    )

    for item in result:
        print(f"Grupo: {item.get('product_group_name')} - Quantidade: {item.get('total')}")


def department_list():
    departments_active = (
        Department.objects.filter(active=True).annotate(total_funcionarios=Count("employee"))
        .order_by("-total_funcionarios")
    )
    for object in departments_active:
        print(f"Departamento: {object.name} - Quantidade: {object.total_funcionarios}")
