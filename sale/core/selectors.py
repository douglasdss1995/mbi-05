from django.db.models import QuerySet
from django.db.models.sql import Query

from core import models
from core.models import Product, Zone, Employee, Customer


def get_all_products():
    return models.Product.objects.all()


def get_all_employees():
    return models.Employee.objects.all()


def get_all_orders():
    return models.Customer.objects.all()


def get_product_by_id(product_id: int):
    return models.Product.objects.get(id=product_id)


def get_product_by_name(name: str):
    return models.Product.objects.get(name=name)


def get_employee_by_name(name: str):
    return models.Employee.objects.get(name=name)


def getcustomer_by_name(name: str):
    return models.Customer.objects.get(name=name)


def create_zone():
    models.Zone.objects.create(name="Zone 1")


def create_product():
    product_group = models.ProductGroup.objects.get(id=1)
    supplier = models.Supplier.objects.get(id=1)

    return models.Product.objects.create(
        name='Produto 01',
        cost_price=1,
        sale_price=2,
        id_supplier=supplier,
        id_product_group=product_group,
        active=True
    )


def deactivate_all_products() -> int:
    # update() atualiza Todos os resgistros de QuerySet de uma vez
    # Equivale a: UPDATE product Set active = false
    # Retorna o numero de linhas afetadas(int)
    # Importante: update() Não chama o metodo save() do model
    # IMPORTANTE: update() NÃO dispara signals (pres_save, post_save)
    return Product.objects.all().update(active=False)


def update_salary_for_all_products(add_percentage: float):
    return Product.objects.all().update(sale_price=add_percetn)

def cout_all_products() -> int:
    return Product.objects.count()




def update_product_sale_price(product_id: int, sale_price: Decimal) -> int:
    """
    atualizar o preço de venda do produto

    Args:
        product_id (int): Id da tabela do produtos
        sale_price (Decimal): Novo calor de venda

    return:
        int: Numero do registro atualizados ( se encontrado,  se nao encontrado)
    """
    return Product.objects.filter(id=product_id).update(sale_price=sale_price)


def update_product_group_gain_percentage(product_group_id: int, new_gain_percentage: Decimal) -> int:
    """
    Atualiza o percentual de lucro de um grupo de produtos

    Args:
        product_group_id (int): Id do grupo de produtos
        new_gain_percentage (Decimal): percentual de lucro de produto
    """

    return Product.objects.filter(id=product_group_id).update(gain_percentage=new_gain_percentage)


def delete_zone_by_id(zone_id: int):
    # delete() remove os registro do QuerySET do bamco

    return Zone.objects.get(id=zone_id).delete()

def count_active_employees() -> int:
    return Employee.objects.(active=True).count()

def count_active_customers() -> int:
    return Customer.objects.(active=True).count()

def has_customer_with_name(name: str) -> bool:
    return Customer.objects.filter(name=name).exists()

def get_first_active_employee() -> Employee | None:
    return Employee.objects.filter(active=True).first()

def get_first_five_product() -> QuerySet[Product]:
    return Product.objects.all()[:5]

def get_products_from_6_to_10() -> QuerySet[Product]:
    return Product.objects.all()[5:10]

def get_high_salary_employees(main_salary: Decimal) -> QuerySet[Employee]:
    return Employee.objects.filter(salary__gte=min_salary)

def get_products_by_name_contains(term: str) -> QuerySet[Product]:
    return Product.objects.filter(name__contains=term)

def get_employees_name_startwith(prefix: str) -> QuerySet[Employee]:
    return Employee.objects.filter(name__istartswith=prefix)

def get_employees_name_startwith(prefix: str) -> int:
    return Employee.objects.filter(name__istartswith=prefix).count()

def count_employees_by_name(name: str) -> int:
    """
    Returns a quantity pelo nome

    Args:
        nome(str): Nome a ser buscado

    Returns:
        int: Quantidade de colaboradores com o nome passado
    """
    return Employee.objects.filter(name=name).count()

def get_customers_with_icome_between() -> QuerySet[Customer]:
    return Customer.objects.all()



