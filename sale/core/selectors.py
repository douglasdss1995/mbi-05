from decimal import Decimal

from django.db.models import QuerySet, Q

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
    return Product.objects.all().update(sale_price=add_percentage)


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
    return Employee.objects.filter(active=True).count()


def count_active_customers() -> int:
    return Customer.objects.filter(active=True).count()


def has_customer_with_name(name: str) -> bool:
    return Customer.objects.filter(name=name).exists()


def get_first_active_employee() -> Employee | None:
    return Employee.objects.filter(active=True).first()


def get_first_five_product() -> QuerySet[Product]:
    return Product.objects.all()[:5]


def get_products_from_6_to_10() -> QuerySet[Product]:
    return Product.objects.all()[5:10]


def get_high_salary_employees(main_salary: Decimal) -> QuerySet[Employee]:
    return Employee.objects.filter(salary__gte=main_salary)


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


def get_products_by_ids(product_ids: list[int]) -> QuerySet[Product]:
    # Busca varios produtos de uma vez pelos IDs
    # Equivale a: SELECT * FROM product WHERE id IN(1,2,3, ...)
    # Mais eficiente que fazer multiplas chamadas a get()
    return Product.objects.filter(id_in=product_ids)


def get_products_by_supplier(supplier_name: str) -> QuerySet[Product]:
    # Navega do Product para o Supplier pelo campo 'id_supplier'
    # '__name__icontains' acessa o campo 'name' do Supplier
    # Equivale a: SELECT p.* FROM product p
    #           JOIN supplier s In p.id_supllier = s.id
    #            WHERE LOWER(s,name)    LIKE LOWER ('%supplier_name%')

    return Product.objects.filter(supplier__name__icontains=supplier_name)


# Por padrao, filter() combina condiçoes com AND
# Para usar o OR ou NOT, voçê precisa do objeto Q().
# Operadores: | (OR), & (AND), ~ (NOT)
def get_products_by_name_or_id(term: str) -> QuerySet[Product]:
    # Busca produtos onde o nome OU ID
    # Equivalente a: SELECTT * FROM product
    #             WHERE nome ILIKE '%term% OR id = %s
    return Product.objects.filter(Q(name__icontains=term) | Q(id=term))


def get_customers_by_filters(
    name: str,
    city: str = None
    ) -> QuerySet[Customer]:
    """Busca clientes pelo nome, e opcionalmente pela cidade. Quando a cidade for fornecida,
    não buscar clientes da Matriz.

    Args:
    name (str): Nome do cliente (busca parcial, case-insensitive)
    city (str): Nome da cidade (busca parcial, case-insensitive)

    Returns :
    QuerySet[Customer]: Clientes que correspondem aos filtros aplicados

    Examples:
    # Busca clientes com "Maria" no nome, independentemente da cidade ou filial
    get_customers_by_filters(name="Maria")

    # Busca clientes com "Maria" no nome, na cidade de "Rio", independentemente da filial
    get_customers_by_filters(name="Maria", city="Rio")
"""
    # Começa com filtro obrigatório pelo nome
    query = Q(name_icontains=name)

    # Adiciona filtro por cidade se fornecido
    if city:
    query &= Q(district_city_name_icontains=city)
    # E garante que não sejam clientes da Matriz (id_district != 1)
    query &= ~Q(district_id=1)

    # Aplica o filtro combinado
    return Customer.objects.filter(query)

def increase_all_salaries(percentage: Decimal) -> int:

    multiplier = 1 + percentage / 100
    return Employee.objects.all().update(salery=F('salary') * multiplier)
    

