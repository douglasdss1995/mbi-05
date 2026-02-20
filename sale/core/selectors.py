from decimal import Decimal
from typing import Any

from django.db.models import QuerySet, Sum, F, Count

from core import models
from core.models import Product, Employee, Department


def get_all_products():
    return models.Product.objects.all()


def get_all_employees():
    return models.Employee.objects.all()


def get_all_customers():
    return models.Customer.objects.all()


def get_product_by_id(product_id: int):
    return models.Product.objects.get(id=product_id)


def get_employee_by_id(employee_id: int):
    return models.Employee.objects.get(id=employee_id)


def get_customer_by_id(customer_id: int):
    return models.Customer.objects.get(id=customer_id)


def get_product(name: str):
    return models.Product.objects.get(name=name)


def get_employee(name: str):
    return models.Employee.objects.get(name=name)


def get_customer_by_name(name: str):
    return models.Customer.objects.get(name=name)


def create_zone():
    models.Zone.objects.create(name='Zona 01')


def create_product():
    product_group = models.ProductGroup.objects.get(id=1)
    suppiler = models.Supplier.objects.get(id=1)
    models.Product.objects.create(
        name='produto 01',
        const_price=1,
        sale_price=1,
        id_suppiler=suppiler,
        id_product_group=product_group,
        active=True

    )


def create_product_group():
    return models.ProductGroup.objects.create(
        name='productGroup',
        commission_percentage=1,
        gain_percentage=1,
    )


def deactivate_product():
    return Product.objects.all().update(active=False)


def uptade_product_group_commission_percentage():
    return models.ProductGroup.objects.filter(id=20).update(
        commission_percentage=0
    )


"""atualize o percentual de lucro de um grupo de produtos
#Args: 
#product_grouo_id

"""


# def update_salary_for_employee(add_percent: Decimal) -> Decimal:
# return models.Employee.objects.all()udpate

def update_product_sale_price(product_id: int, sale_price: Decimal) -> int:
    return models.Product.objects.filter(product_id=product_id).update(
        sale_price=sale_price
    )


def uddate_product_group_gain_percentage(product_group_id: int, gain_percentage: Decimal) -> int:
    return models.ProductGroup.objects.filter(id=product_group_id).update(
        gain_percentage=gain_percentage
    )


def delete_zone_by_id(zone_id: int):
    return models.Zone.objects.filter(id=zone_id).delete()


def count_all_products() -> int:
    return models.Product.objects.count()


def count_active_employees() -> int:
    return models.Employee.objects.filter(active=True).count()


def count_active_customers() -> int:
    return models.Customer.objects.filter(active=True).count()


def has_eny_product() -> bool:
    return models.Product.objects.exists()


def has_customer_with_name(name: str) -> bool:
    return models.Customer.objects.filter(name=name).exists()


def get_firts_acttive_employee() -> Employee | None:
    return models.Employee.objects.filter(active=True).first()


def get_firts_five_products() -> QuerySet[models.Product]:
    return models.Product.objects.all()[:5]


def get_products_from_6_to_10() -> QuerySet[Product]:
    return models.Product.objects.all()[5:10]


def get_hifh_employees(min_salary: Decimal) -> QuerySet[Employee]:
    return models.Employee.objects.filter(salary__gte=min_salary)


def get_products_by_name_contains(term: str) -> QuerySet[Product]:
    return models.Product.objects.filter(name__icontains=term)


def get_employees_name_startswith(prefix: str) -> QuerySet[Employee]:
    return models.Employee.objects.filter(name__startswith=prefix)


def get_employees_name_endswith(prefix: str) -> QuerySet[Employee]:
    return models.Employee.objects.filter(name__endswith=prefix).count()


def count_employees_by_name_name(name: str) -> int:
    usuarios = models.Employee.objects.filter(name__icontains=name, active=True)
    return usuarios.count()


def get_total_employee_salary() -> dict:
    return models.Employee.objects.aggregate(Sum('salary'))


def get_total_employee_witch_salary() -> dict:
    return models.Employee.objects.aggregate(total=Sum('salary'))


def get_branch_sales(branch_id: int) -> Decimal:
    return models.Branch.objects.filter(id=branch_id).aggregate(
        total_sale=Sum(
            F("sales__sale_items__quantity") * F("sales__sale_items__sale_price")
        ),
    )["total_sale"] or Decimal(value="0.00")


def get_departaments_with_employee_count() -> QuerySet[Department]:
    return models.Department.objects.annotate(
        total_employees=Count('employee')
    )


def get_product_id_and_name() -> QuerySet[Product, dict[str, Any]]:
    return models.Product.objects.values_list("id", "name")


def get_products_with_renamed_field() -> QuerySet[Product, dict[str, Any]]:
    return models.Product.objects.values(
        product_id=F("id"),
        product_name=F("name"),
        group_name=F("product_group__name"),
        suppiler_name=F("supplier__name"),
        price=F("sale_price"),
    )


def get_product_count_by_group() -> QuerySet[Product, dict[str, int]]:
    return models.Product.objects.values("product_group__name").annotate(
        total_products=Count("id"),
    )


def get_branch_sale():
    vendas = models.Branch.objects.values("name").annotate(
        total_sale=Sum(
            F("sales__sale_items__quantity") * F("sales__sale_items__sale_price")
        )
    )

    for items in venda
