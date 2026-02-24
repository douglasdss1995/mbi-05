"""
=============================================================================
AULA: QuerySets no Django
=============================================================================
QuerySet é a representação de uma consulta ao banco de dados.
Ele é LAZY, ou seja, só executa a query quando os dados são realmente
necessários (iteração, slicing, repr, list(), etc).

Usaremos os modelos do nosso projeto de vendas para exemplificar.
=============================================================================
"""

from datetime import date
from decimal import Decimal
from os import name
from typing import Any

from django.db.models import (
    Avg,
    Count,
    ExpressionWrapper,
    F,
    Max,
    Min,
    Q,
    QuerySet,
    Sum,
    Value,
)
from django.db.models.fields import DecimalField as DecimalFieldType

from core.models import (
    Customer,
    Department,
    Employee,
    Product,
    ProductGroup,
    Sale,
    SaleItem,
    State,
    Supplier,
    Zone, Branch,
)


# =============================================================================
# all() — Retorna todos os registros da tabela
# =============================================================================
def get_all_products() -> QuerySet[Product]:
    # all() retorna um QuerySet com TODOS os registros da tabela 'product'
    # Equivale a: SELECT * FROM product
    # Lembre-se: o QuerySet é lazy, a query só roda quando você consumir os dados
    return Product.objects.all()


def get_all_employees() -> QuerySet[Employee]:
    # Retorna todos os funcionários cadastrados
    # Equivale a: SELECT * FROM employee
    return Employee.objects.all()


def get_all_customers() -> QuerySet[Customer]:
    # Retorna todos os clientes cadastrados
    # Equivale a: SELECT * FROM customer
    return Customer.objects.all()


# =============================================================================
# get() — Retorna UM ÚNICO objeto que corresponda aos filtros
# =============================================================================
def get_product_by_id(product_id: int) -> Product:
    # get() retorna exatamente UM objeto
    # Equivale a: SELECT * FROM product WHERE id = %s LIMIT 1
    # CUIDADO: Lança 'Product.DoesNotExist' se não encontrar nenhum registro
    # CUIDADO: Lança 'Product.MultipleObjectsReturned' se encontrar mais de um
    return Product.objects.get(id=product_id)


def get_employee_by_id(employee_id: int) -> Employee:
    # Busca um funcionário pelo ID — retorna exatamente um objeto
    # Se o ID não existir, lança Employee.DoesNotExist
    return Employee.objects.get(id=employee_id)


def get_employee_by_name(name: str) -> Employee:
    # Busca um funcionário pelo nome EXATO
    # Se houver mais de um funcionário com o mesmo nome, lança MultipleObjectsReturned
    # Use get() apenas quando você tem CERTEZA de que o resultado será único
    return Employee.objects.get(name=name)


def get_customer_by_name(name: str) -> Customer:
    # Busca um cliente pelo nome EXATO
    # Se houver mais de um cliente com o mesmo nome, lança MultipleObjectsReturned
    # Use get() apenas quando você tem CERTEZA de que o resultado será único
    return Customer.objects.get(name=name)


# =============================================================================
# filter() — Retorna um QuerySet com os registros que correspondem aos filtros
# =============================================================================
def get_active_employees() -> QuerySet[Employee]:
    # filter() retorna um QuerySet com os registros que CORRESPONDEM ao critério
    # Equivale a: SELECT * FROM employee WHERE active = true
    return Employee.objects.filter(active=True)


def get_employees_by_department(department_id: int) -> QuerySet[Employee]:
    # Filtra funcionários pelo ID do departamento usando a relação ForeignKey
    # Equivale a: SELECT * FROM employee WHERE id_department = %s
    return Employee.objects.filter(department_id=department_id)


# =============================================================================
# order_by() — Ordena os registros por um ou mais campos
# =============================================================================
def get_products_ordered_by_price() -> QuerySet[Product]:
    # order_by() ordena os registros pelo campo especificado
    # Equivale a: SELECT * FROM product ORDER BY sale_price ASC
    # Para ordem decrescente, use '-' antes do nome do campo: order_by('-sale_price')
    return Product.objects.order_by("sale_price")


# =============================================================================
# create() — Cria e salva um novo registro no banco de dados
# =============================================================================
def create_department(name: str) -> Department:
    # create() cria o objeto E já salva no banco em uma única operação
    # Equivale a: INSERT INTO department (name) VALUES (%s)
    # Diferente de instanciar o model e depois chamar .save()
    return Department.objects.create(
        name=name,  # Nome do departamento
    )


def create_zone(name: str) -> Zone:
    # Cria uma nova zona e já persiste no banco
    # O objeto retornado já possui o ID gerado pelo banco
    return Zone.objects.create(
        name=name,
    )


def create_product_group(
    name: str,
    commission_percentage: Decimal,
    gain_percentage: Decimal,
) -> ProductGroup:
    # Cria um grupo de produto com seus percentuais
    # Todos os campos obrigatórios devem ser informados
    return ProductGroup.objects.create(
        name=name,  # Nome do grupo
        commission_percentage=commission_percentage,  # Percentual de comissão
        gain_percentage=gain_percentage,  # Percentual de lucro
    )


def create_state(
    name: str,
    abbreviation: str,
) -> State:
    # Cria um novo estado com nome e sigla
    # Exemplo: create_state('São Paulo', 'SP')
    return State.objects.create(
        name=name,
        abbreviation=abbreviation,
    )


def create_supplier(
    name: str,
    legal_document: str,
) -> Supplier:
    # Cria um fornecedor com CNPJ/CPF
    # legal_document é unique — tentar criar duplicado lança IntegrityError
    return Supplier.objects.create(
        name=name,
        legal_document=legal_document,
    )


def create_product(
    name: str,
    cost_price: Decimal,
    sale_price: Decimal,
    product_group: ProductGroup,
    supplier: Supplier,
) -> Product:
    # Cria um novo produto com os dados fornecidos
    return Product.objects.create(
        name=name,
        cost_price=cost_price,
        sale_price=sale_price,
        product_group=product_group,
        supplier=supplier,
    )


# =============================================================================
# update() — Atualiza registros em massa (opera no QuerySet, não no objeto)
# =============================================================================
def deactivate_all_products() -> int:
    # update() atualiza TODOS os registros do QuerySet de uma vez
    # Equivale a: UPDATE product SET active = false
    # Retorna o número de linhas afetadas (int)
    # IMPORTANTE: update() NÃO chama o método save() do model
    # IMPORTANTE: update() NÃO dispara signals (pre_save, post_save)
    return Product.objects.all().update(active=False)


def update_product_group_commission(group_id: int, new_commission: Decimal) -> int:
    # Atualiza o percentual de comissão de um grupo específico
    # Equivale a: UPDATE product_group SET commission_percentage = %s WHERE id = %s
    return ProductGroup.objects.filter(id=group_id).update(
        commission_percentage=new_commission,
    )


def activate_department_by_id(department_id: int) -> int:
    # Filtra pelo ID e atualiza apenas aquele registro
    # Equivale a: UPDATE department SET active = true WHERE id = %s
    # Retorna 1 se encontrou e atualizou, 0 se não encontrou
    return Department.objects.filter(id=department_id).update(active=True)


def update_employee_salary(employee_id: int, new_salary: Decimal) -> int:
    # Atualiza o salário de um funcionário específico
    # Equivale a: UPDATE employee SET salary = %s WHERE id = %s
    return Employee.objects.filter(id=employee_id).update(salary=new_salary)


def deactivate_customers_by_gender(gender: str) -> int:
    # Atualiza múltiplos registros de uma vez com base em um filtro
    # Equivale a: UPDATE customer SET active = false WHERE gender = %s
    # Exemplo: deactivate_customers_by_gender('M') desativa todos os clientes masculinos
    return Customer.objects.filter(gender=gender).update(active=False)


# =============================================================================
# delete() — Remove registros do banco de dados
# =============================================================================
def delete_zone_by_id(zone_id: int) -> tuple:
    # delete() remove os registros do QuerySet do banco
    # Equivale a: DELETE FROM zone WHERE id = %s
    # Retorna uma tupla: (total_deletado, {detalhamento_por_model})
    # Exemplo de retorno: (1, {'core.Zone': 1})
    # CUIDADO: se houver ForeignKey com RESTRICT, lança ProtectedError
    return Zone.objects.filter(id=zone_id).delete()


def delete_inactive_departments() -> tuple:
    # Remove TODOS os departamentos inativos de uma vez
    # Equivale a: DELETE FROM department WHERE active = false
    # CUIDADO: delete() em massa NÃO chama o método delete() do model individual
    # CUIDADO: delete() em massa NÃO dispara signals (pre_delete, post_delete)
    return Department.objects.filter(active=False).delete()


def delete_single_product(product_id: int) -> tuple:
    # Outra forma: buscar o objeto com get() e chamar delete() nele
    # Essa forma DISPARA os signals (pre_delete, post_delete)
    # Porém, faz duas queries: uma SELECT + uma DELETE
    product = Product.objects.get(id=product_id)
    return product.delete()


# =============================================================================
# count() — Conta o número de registros
# =============================================================================
def count_all_products() -> int:
    # count() retorna o número total de registros no QuerySet
    # Equivale a: SELECT COUNT(*) FROM product
    # Mais eficiente que len(Product.objects.all()) pois a contagem é feita no banco
    return Product.objects.count()


def count_active_employees() -> int:
    # Conta apenas funcionários ativos usando filter + count
    # Equivale a: SELECT COUNT(*) FROM employee WHERE active = true
    return Employee.objects.filter(active=True).count()


def count_customers_by_gender(gender: str) -> int:
    # Conta clientes por gênero
    # Exemplo: count_customers_by_gender('F') conta todas as clientes femininas
    # Equivale a: SELECT COUNT(*) FROM customer WHERE gender = %s
    return Customer.objects.filter(gender=gender).count()


# =============================================================================
# exists() — Verifica se existe pelo menos um registro
# =============================================================================
def has_any_product() -> bool:
    # exists() retorna True se houver pelo menos UM registro, False caso contrário
    # Equivale a: SELECT 1 FROM product LIMIT 1
    # Mais eficiente que count() > 0, pois para na primeira ocorrência
    return Product.objects.exists()


def has_active_employees() -> bool:
    # Verifica se existe pelo menos um funcionário ativo
    # Equivale a: SELECT 1 FROM employee WHERE active = true LIMIT 1
    return Employee.objects.filter(active=True).exists()


def has_customer_with_name(name: str) -> bool:
    # Verifica se existe algum cliente com determinado nome
    # Útil para validações antes de criar registros
    # Equivale a: SELECT 1 FROM customer WHERE name = %s LIMIT 1
    return Customer.objects.filter(name=name).exists()


def has_high_income_customers(min_income: Decimal) -> bool:
    # Verifica se existe algum cliente com renda acima do valor informado
    # '__gte' significa 'greater than or equal' (maior ou igual)
    # Equivale a: SELECT 1 FROM customer WHERE income >= %s LIMIT 1
    return Customer.objects.filter(income__gte=min_income).exists()


# =============================================================================
# first() — Retorna o primeiro registro do QuerySet (ou None)
# =============================================================================
def get_first_product() -> Product | None:
    # first() retorna o PRIMEIRO objeto do QuerySet ou None se estiver vazio
    # Equivale a: SELECT * FROM product ORDER BY ... LIMIT 1
    # A ordem depende do 'ordering' definido na Meta do model
    # Nunca lança exceção, ao contrário de get()
    return Product.objects.first()


def get_first_active_employee() -> Employee | None:
    # Retorna o primeiro funcionário ativo (pela ordem padrão do model)
    # Retorna None se não houver nenhum funcionário ativo
    return Employee.objects.filter(active=True).first()


def get_cheapest_product() -> Product | None:
    # Combina order_by() com first() para pegar o produto mais barato
    # order_by('sale_price') ordena do menor para o maior preço
    # first() pega o primeiro da lista (o mais barato)
    # Equivale a: SELECT * FROM product ORDER BY sale_price ASC LIMIT 1
    return Product.objects.order_by("sale_price").first()


# =============================================================================
# last() — Retorna o último registro do QuerySet (ou None)
# =============================================================================
def get_last_product() -> Product | None:
    # last() retorna o ÚLTIMO objeto do QuerySet ou None se estiver vazio
    # Equivale a: SELECT * FROM product ORDER BY ... DESC LIMIT 1
    # A ordem depende do 'ordering' definido na Meta do model
    # IMPORTANTE: para funcionar corretamente, o QuerySet deve estar ordenado
    return Product.objects.last()


def get_last_active_employee() -> Employee | None:
    # Retorna o último funcionário ativo
    # Retorna None se não houver nenhum funcionário ativo
    return Employee.objects.filter(active=True).last()


def get_most_expensive_product() -> Product | None:
    # Combina order_by() com last() para pegar o produto mais caro
    # order_by('sale_price') ordena do menor para o maior
    # last() pega o último (o mais caro)
    # Equivale a: SELECT * FROM product ORDER BY sale_price ASC LIMIT 1 OFFSET (COUNT-1)
    # Alternativa mais eficiente: order_by('-sale_price').first()
    return Product.objects.order_by("sale_price").last()


# =============================================================================
# Slicing — Fatiar o QuerySet como uma lista Python
# =============================================================================
def get_first_five_products() -> QuerySet[Product]:
    # Slicing funciona como em listas Python: [inicio:fim]
    # [:5] retorna os 5 primeiros registros
    # Equivale a: SELECT * FROM product LIMIT 5
    # IMPORTANTE: slicing NÃO suporta índices negativos
    return Product.objects.all()[:5]


def get_products_from_6_to_10() -> QuerySet[Product]:
    # [5:10] pula os 5 primeiros e retorna os próximos 5
    # Equivale a: SELECT * FROM product LIMIT 5 OFFSET 5
    # Útil para implementar paginação manual
    return Product.objects.all()[5:10]


def get_single_product_by_index(index: int) -> Product:
    # [index] retorna UM único objeto (não um QuerySet)
    # Equivale a: SELECT * FROM product LIMIT 1 OFFSET %s
    # CUIDADO: lança IndexError se o índice estiver fora do range
    return Product.objects.all()[index]


def get_first_three_employees_by_salary() -> QuerySet[Employee]:
    # Combina order_by() com slicing para pegar os 3 funcionários com menor salário
    # Primeiro ordena por salário crescente, depois fatia os 3 primeiros
    # Equivale a: SELECT * FROM employee ORDER BY salary ASC LIMIT 3
    return Employee.objects.order_by("salary")[:3]


def get_top_three_highest_paid_employees() -> QuerySet[Employee]:
    # '-salary' ordena do maior para o menor (decrescente)
    # [:3] pega os 3 primeiros (os 3 com maior salário)
    # Equivale a: SELECT * FROM employee ORDER BY salary DESC LIMIT 3
    return Employee.objects.order_by("-salary")[:3]


# =============================================================================
# Encadeamento de métodos (QuerySet chaining)
# =============================================================================
def get_active_female_customers() -> QuerySet[Customer]:
    # QuerySets podem ser ENCADEADOS: cada método retorna um novo QuerySet
    # filter() pode ser chamado múltiplas vezes — os filtros se acumulam com AND
    # Equivale a: SELECT * FROM customer WHERE active = true AND gender = 'F'
    return (
        Customer.objects.filter(active=True).filter(  # Primeiro filtra por ativos
            gender="F"
        )  # Depois filtra por gênero feminino
    )


def get_active_male_customers_ordered() -> QuerySet[Customer]:
    # Encadeia filter, order_by e slicing em uma única expressão
    # Equivale a: SELECT * FROM customer WHERE active = true AND gender = 'M'
    #             ORDER BY name ASC LIMIT 10
    return (
        Customer.objects.filter(active=True)  # Filtra apenas ativos
        .filter(gender="M")  # Filtra apenas masculinos
        .order_by("name")[
            # Ordena por nome A-Z
            :10
        ]  # Pega apenas os 10 primeiros
    )


# =============================================================================
# BÔNUS — Diferença entre filter() e exclude()
# =============================================================================
def get_active_products() -> QuerySet[Product]:
    # filter() retorna registros que CORRESPONDEM ao critério
    # Equivale a: SELECT * FROM product WHERE active = true
    return Product.objects.filter(active=True)


def get_active_products_with_exclude() -> QuerySet[Product]:
    # exclude() retorna registros que NÃO correspondem ao critério
    # Equivale a: SELECT * FROM product WHERE NOT (active = false)
    # O resultado é o mesmo de filter(active=True), mas a lógica é invertida
    return Product.objects.exclude(active=False)


# =============================================================================
# Lookups de campo (field lookups)
# =============================================================================
# No Django, lookup expressions são sufixos adicionados ao nome do campo
# usando duplo underscore (__) para definir o TIPO de comparação.
# Sem lookup, o Django assume '__exact' por padrão.
def get_high_salary_employees(min_salary: Decimal) -> QuerySet[Employee]:
    # '__gte' = greater than or equal (maior ou igual)
    # Equivale a: SELECT * FROM employee WHERE salary >= %s
    return Employee.objects.filter(salary__gte=min_salary)


def get_products_by_name_contains(term: str) -> QuerySet[Product]:
    # '__icontains' = busca case-insensitive (ignora maiúsculas/minúsculas)
    # Equivale a: SELECT * FROM product WHERE LOWER(name) LIKE LOWER('%term%')
    return Product.objects.filter(name__icontains=term)


def get_products_in_price_range(
    min_price: Decimal,
    max_price: Decimal,
) -> QuerySet[Product]:
    # '__gte' = maior ou igual, '__lte' = menor ou igual
    # Múltiplos filtros no mesmo filter() funcionam como AND
    # Equivale a: SELECT * FROM product WHERE sale_price >= %s AND sale_price <= %s
    return Product.objects.filter(
        sale_price__gte=min_price,
        sale_price__lte=max_price,
    )


def get_employees_name_startswith(prefix: str) -> QuerySet[Employee]:
    # '__istartswith' = nome começa com o prefixo (case-insensitive)
    # Equivale a: SELECT * FROM employee WHERE LOWER(name) LIKE LOWER('prefix%')
    return Employee.objects.filter(name__istartswith=prefix)


def get_customers_with_income_between(
    min_income: Decimal,
    max_income: Decimal,
) -> QuerySet[Customer]:
    # '__range' = entre dois valores (inclusivo nos dois extremos)
    # Equivale a: SELECT * FROM customer WHERE income BETWEEN %s AND %s
    return Customer.objects.filter(income__range=(min_income, max_income))


# =============================================================================
# exact e iexact (correspondência exata)
# =============================================================================
def get_state_by_abbreviation(abbreviation: str) -> QuerySet[State]:
    # '__exact' é o lookup PADRÃO — você não precisa escrevê-lo
    # Estas duas linhas são IDÊNTICAS:
    #   State.objects.filter(abbreviation='SP')
    #   State.objects.filter(abbreviation__exact='SP')
    # Equivale a: SELECT * FROM state WHERE abbreviation = %s
    return State.objects.filter(abbreviation__exact=abbreviation)


def get_customer_by_name_case_insensitive(name: str) -> QuerySet[Customer]:
    # '__iexact' faz comparação exata, mas IGNORA maiúsculas/minúsculas
    # O 'i' no início significa 'insensitive' (case-insensitive)
    # Equivale a: SELECT * FROM customer WHERE LOWER(name) = LOWER(%s)
    # Exemplo: 'joão silva' encontra 'João Silva', 'JOÃO SILVA', etc.
    return Customer.objects.filter(name__iexact=name)


def get_employees_by_gender_exact(gender: str) -> QuerySet[Employee]:
    # Busca exata por gênero — como é campo curto, exact é o ideal
    # Equivale a: SELECT * FROM employee WHERE gender = %s
    return Employee.objects.filter(gender__exact=gender)


# =============================================================================
# contains e icontains (contém texto)
# =============================================================================
# 'contains' busca texto que CONTENHA o termo (case-sensitive)
# 'icontains' faz o mesmo, mas ignorando maiúsculas/minúsculas
def get_products_name_contains_case_sensitive(term: str) -> QuerySet[Product]:
    # '__contains' busca CASE-SENSITIVE — 'café' NÃO encontra 'Café'
    # Equivale a: SELECT * FROM product WHERE name LIKE '%term%'
    # Use quando a diferença entre maiúsculas e minúsculas importa
    return Product.objects.filter(name__contains=term)


def get_suppliers_name_contains(term: str) -> QuerySet[Supplier]:
    # '__icontains' busca CASE-INSENSITIVE — 'café' encontra 'Café', 'CAFÉ', etc.
    # Equivale a: SELECT * FROM supplier WHERE LOWER(name) LIKE LOWER('%term%')
    # Na maioria dos casos, icontains é o que você quer para buscas de texto
    return Supplier.objects.filter(name__icontains=term)


# =============================================================================
# startswith, istartswith, endswith, iendswith
# =============================================================================
# Buscam texto que COMEÇA ou TERMINA com determinado valor
def get_customers_name_startswith(prefix: str) -> QuerySet[Customer]:
    # '__startswith' = nome começa com o prefixo (CASE-SENSITIVE)
    # Equivale a: SELECT * FROM customer WHERE name LIKE 'prefix%'
    return Customer.objects.filter(name__startswith=prefix)


def get_products_name_endswith(suffix: str) -> QuerySet[Product]:
    # '__endswith' = nome termina com o sufixo (CASE-SENSITIVE)
    # Equivale a: SELECT * FROM product WHERE name LIKE '%suffix'
    return Product.objects.filter(name__endswith=suffix)


def get_products_name_iendswith(suffix: str) -> QuerySet[Product]:
    # '__iendswith' = nome termina com o sufixo (CASE-INSENSITIVE)
    # Equivale a: SELECT * FROM product WHERE LOWER(name) LIKE LOWER('%suffix')
    # Exemplo: 'ml' encontra 'Leite 500ML', 'Suco 1000ml', etc.
    return Product.objects.filter(name__iendswith=suffix)


def get_states_abbreviation_startswith(prefix: str) -> QuerySet[State]:
    # Busca estados cuja sigla começa com determinada letra
    # Exemplo: 'S' encontra 'SP', 'SC', 'SE', etc.
    # Equivale a: SELECT * FROM state WHERE abbreviation LIKE 'prefix%'
    return State.objects.filter(abbreviation__startswith=prefix)


# =============================================================================
# Lookup Expressions — gt e lt (maior que / menor que estrito)
# =============================================================================
# '__gt' = greater than (estritamente maior)
# '__lt' = less than (estritamente menor)
# Diferente de __gte e __lte que INCLUEM o valor da comparação
def get_products_above_price(price: Decimal) -> QuerySet[Product]:
    # '__gt' = estritamente MAIOR que (não inclui o valor)
    # Equivale a: SELECT * FROM product WHERE sale_price > %s
    # Se price=100, retorna produtos com preço 100.01 em diante (100 NÃO entra)
    return Product.objects.filter(sale_price__gt=price)


def get_products_below_price(price: Decimal) -> QuerySet[Product]:
    # '__lt' = estritamente MENOR que (não inclui o valor)
    # Equivale a: SELECT * FROM product WHERE sale_price < %s
    # Se price=50, retorna produtos com preço até 49.99 (50 NÃO entra)
    return Product.objects.filter(sale_price__lt=price)


def get_products_with_profit_margin() -> QuerySet[Product]:
    # Produtos onde o preço de venda é MAIOR que o preço de custo
    # Equivale a: SELECT * FROM product WHERE sale_price > cost_price
    # Usa F() para comparar dois campos do MESMO model
    return Product.objects.filter(sale_price__gt=F("cost_price"))


def get_employees_salary_below(max_salary: Decimal) -> QuerySet[Employee]:
    # Funcionários com salário estritamente menor que o valor informado
    # Equivale a: SELECT * FROM employee WHERE salary < %s
    return Employee.objects.filter(salary__lt=max_salary)


# =============================================================================
# in (está na lista)
# =============================================================================
# '__in' verifica se o valor do campo está em uma lista de valores
def get_products_by_ids(product_ids: list[int]) -> QuerySet[Product]:
    # Busca vários produtos de uma vez pelos IDs
    # Equivale a: SELECT * FROM product WHERE id IN (1, 2, 3, ...)
    # Mais eficiente que fazer múltiplas chamadas a get()
    return Product.objects.filter(id__in=product_ids)


def get_states_by_abbreviations(abbreviations: list[str]) -> QuerySet[State]:
    # Busca estados por uma lista de siglas
    # Equivale a: SELECT * FROM state WHERE abbreviation IN ('SP', 'RJ', 'MG')
    # Exemplo: get_states_by_abbreviations(['SP', 'RJ', 'MG'])
    return State.objects.filter(abbreviation__in=abbreviations)


def get_employees_from_departments(department_ids: list[int]) -> QuerySet[Employee]:
    # '__in' também funciona com ForeignKey — filtra pelo ID da relação
    # Equivale a: SELECT * FROM employee WHERE id_department IN (1, 2, 3)
    return Employee.objects.filter(department__in=department_ids)


# =============================================================================
# Lookup Expressions — isnull (campo é nulo)
# =============================================================================
# '__isnull' verifica se o campo é NULL (True) ou NOT NULL (False)
def get_sale_items_without_price() -> QuerySet[SaleItem]:
    # '__isnull=True' filtra registros onde o campo É NULO
    # Equivale a: SELECT * FROM sale_item WHERE sale_price IS NULL
    # Útil para encontrar dados incompletos
    return SaleItem.objects.filter(sale_price__isnull=True)


def get_sale_items_with_price() -> QuerySet[SaleItem]:
    # '__isnull=False' filtra registros onde o campo NÃO é nulo
    # Equivale a: SELECT * FROM sale_item WHERE sale_price IS NOT NULL
    return SaleItem.objects.filter(sale_price__isnull=False)


# =============================================================================
# date, year, month, day (lookups temporais)
# =============================================================================
# Lookups para campos DateField e DateTimeField permitem filtrar por
# partes específicas da data
def get_employees_hired_in_year(year: int) -> QuerySet[Employee]:
    # '__year' extrai o ANO do campo de data
    # Equivale a: SELECT * FROM employee WHERE EXTRACT(YEAR FROM admission_date) = %s
    # Exemplo: get_employees_hired_in_year(2024)
    return Employee.objects.filter(admission_date__year=year)


def get_employees_hired_in_month(month: int) -> QuerySet[Employee]:
    # '__month' extrai o MÊS do campo de data (1-12)
    # Equivale a: SELECT * FROM employee WHERE EXTRACT(MONTH FROM admission_date) = %s
    # Exemplo: get_employees_hired_in_month(12) — contratados em dezembro
    return Employee.objects.filter(admission_date__month=month)


def get_employees_born_on_day(day: int) -> QuerySet[Employee]:
    # '__day' extrai o DIA do campo de data (1-31)
    # Equivale a: SELECT * FROM employee WHERE EXTRACT(DAY FROM birth_date) = %s
    # Exemplo: get_employees_born_on_day(25) — nascidos no dia 25
    return Employee.objects.filter(birth_date__day=day)


def get_employees_hired_in_year_and_month(
    year: int,
    month: int,
) -> QuerySet[Employee]:
    # Podemos ENCADEAR lookups de data para filtrar com precisão
    # Equivale a: SELECT * FROM employee
    #             WHERE EXTRACT(YEAR FROM admission_date) = %s
    #             AND EXTRACT(MONTH FROM admission_date) = %s
    return Employee.objects.filter(
        admission_date__year=year,
        admission_date__month=month,
    )


def get_sales_on_date(target_date: date) -> QuerySet[Sale]:
    # '__date' extrai apenas a parte DATE de um DateTimeField
    # Útil quando o campo é DateTime mas você quer filtrar só pela data
    # Equivale a: SELECT * FROM sale WHERE DATE(date) = %s
    return Sale.objects.filter(date__date=target_date)


def get_sales_in_year(year: int) -> QuerySet[Sale]:
    # '__year' funciona tanto em DateField quanto em DateTimeField
    # Equivale a: SELECT * FROM sale WHERE EXTRACT(YEAR FROM date) = %s
    return Sale.objects.filter(date__year=year)


def get_employees_hired_before_year(year: int) -> QuerySet[Employee]:
    # Lookups de data podem ser COMBINADOS com outros lookups!
    # '__year__lt' = ano MENOR que o valor informado
    # Equivale a: SELECT * FROM employee WHERE EXTRACT(YEAR FROM admission_date) < %s
    return Employee.objects.filter(admission_date__year__lt=year)


def get_employees_born_after(ref_date: date) -> QuerySet[Employee]:
    # '__gt' funciona diretamente em DateField para comparar datas completas
    # Equivale a: SELECT * FROM employee WHERE birth_date > %s
    return Employee.objects.filter(birth_date__gt=ref_date)


# =============================================================================
# Lookup Expressions — week_day e week (lookups temporais avançados)
# =============================================================================
def get_employees_hired_on_weekday(weekday: int) -> QuerySet[Employee]:
    # '__week_day' retorna o dia da semana (1=Domingo, 2=Segunda, ..., 7=Sábado)
    # ATENÇÃO: a contagem começa no Domingo (padrão americano)
    # Equivale a: SELECT * FROM employee WHERE DAYOFWEEK(admission_date) = %s
    # Exemplo: get_employees_hired_on_weekday(2) — contratados na segunda-feira
    return Employee.objects.filter(admission_date__week_day=weekday)


def get_sales_in_week(week: int) -> QuerySet[Sale]:
    # '__week' retorna o número da semana ISO do ano (1-52/53)
    # Equivale a: SELECT * FROM sale WHERE EXTRACT(WEEK FROM date) = %s
    # Exemplo: get_sales_in_week(1) — vendas na primeira semana do ano
    return Sale.objects.filter(date__week=week)


# =============================================================================
# Lookup Expressions — regex e iregex (expressões regulares)
# =============================================================================
# Permitem buscas usando expressões regulares — mais poderosas que contains
def get_products_name_regex(pattern: str) -> QuerySet[Product]:
    # '__regex' faz busca com expressão regular (CASE-SENSITIVE)
    # Equivale a: SELECT * FROM product WHERE name ~ 'pattern' (PostgreSQL)
    # Exemplo: get_products_name_regex(r'^[ABC]') — nomes que começam com A, B ou C
    return Product.objects.filter(name__regex=pattern)


def get_products_name_iregex(pattern: str) -> QuerySet[Product]:
    # '__iregex' faz busca com expressão regular (CASE-INSENSITIVE)
    # Equivale a: SELECT * FROM product WHERE name ~* 'pattern' (PostgreSQL)
    # Exemplo: get_products_name_iregex(r'leite|suco') — contêm "leite" ou "suco"
    return Product.objects.filter(name__iregex=pattern)


def get_employees_name_matches_pattern(pattern: str) -> QuerySet[Employee]:
    # Regex é útil quando contains/startswith não são suficientes
    # Exemplo: r'^Maria\s' encontra "Maria Silva", "Maria Santos"
    #          mas NÃO encontra "Mariana" (pois exige espaço depois de Maria)
    return Employee.objects.filter(name__iregex=pattern)


def get_suppliers_legal_document_pattern(pattern: str) -> QuerySet[Supplier]:
    # Regex para validar formato de CNPJ/CPF
    # Exemplo: r'^\d{2}\.\d{3}\.\d{3}' encontra documentos no formato XX.XXX.XXX...
    return Supplier.objects.filter(legal_document__regex=pattern)


# =============================================================================
# Lookups em Relacionamentos (spanning relationships)
# =============================================================================
# O Django permite navegar por ForeignKey usando duplo underscore (__)
# Isso gera JOINs automaticamente no SQL
def get_products_by_supplier_name(supplier_name: str) -> QuerySet[Product]:
    # Navega do Product para o Supplier pelo campo 'id_supplier'
    # '__name__icontains' acessa o campo 'name' do Supplier
    # Equivale a: SELECT p.* FROM product p
    #             JOIN supplier s ON p.id_supplier = s.id
    #             WHERE LOWER(s.name) LIKE LOWER('%supplier_name%')
    return Product.objects.filter(supplier__name__icontains=supplier_name)


def get_products_by_group_name(group_name: str) -> QuerySet[Product]:
    # Navega do Product para o ProductGroup
    # Equivale a: SELECT p.* FROM product p
    #             JOIN product_group pg ON p.id_product_group = pg.id
    #             WHERE LOWER(pg.name) LIKE LOWER('%group_name%')
    return Product.objects.filter(product_group__name__icontains=group_name)


def get_employees_by_department_name(
    department_name: str,
) -> QuerySet[Employee]:
    # Busca funcionários pelo nome do departamento
    # Equivale a: SELECT e.* FROM employee e
    #             JOIN department d ON e.id_department = d.id
    #             WHERE LOWER(d.name) LIKE LOWER('%department_name%')
    return Employee.objects.filter(
        department__name__icontains=department_name,
    )


def get_customers_by_city_name(city_name: str) -> QuerySet[Customer]:
    # Navega por MÚLTIPLOS relacionamentos: Customer -> District -> City
    # Cada '__' navega para a próxima tabela
    # Equivale a: SELECT c.* FROM customer c
    #             JOIN district d ON c.id_district = d.id
    #             JOIN city ci ON d.id_city = ci.id
    #             WHERE LOWER(ci.name) LIKE LOWER('%city_name%')
    return Customer.objects.filter(
        district__city__name__icontains=city_name,
    )


def get_customers_by_state_abbreviation(
    abbreviation: str,
) -> QuerySet[Customer]:
    # Navega por TRÊS relacionamentos: Customer -> District -> City -> State
    # Django gera os JOINs automaticamente, não importa a profundidade
    # Equivale a: SELECT c.* FROM customer c
    #             JOIN district d ON c.id_district = d.id
    #             JOIN city ci ON d.id_city = ci.id
    #             JOIN state s ON ci.id_state = s.id
    #             WHERE s.abbreviation = %s
    return Customer.objects.filter(
        district__city__state__abbreviation=abbreviation,
    )


def get_employees_in_zone(zone_name: str) -> QuerySet[Employee]:
    # Navega: Employee -> District -> Zone
    # Equivale a: SELECT e.* FROM employee e
    #             JOIN district d ON e.id_district = d.id
    #             JOIN zone z ON d.id_zone = z.id
    #             WHERE LOWER(z.name) LIKE LOWER('%zone_name%')
    return Employee.objects.filter(
        district__zone__name__icontains=zone_name,
    )


def get_products_by_supplier_active_status(
    is_active: bool,
) -> QuerySet[Product]:
    # Lookup em relacionamento com campo booleano
    # Equivale a: SELECT p.* FROM product p
    #             JOIN supplier s ON p.id_supplier = s.id
    #             WHERE s.active = %s
    return Product.objects.filter(supplier__active=is_active)


def get_products_by_group_min_commission(
    min_commission: Decimal,
) -> QuerySet[Product]:
    # Combina lookup de relacionamento com lookup de comparação
    # Navega para ProductGroup e filtra por commission_percentage >= valor
    # Equivale a: SELECT p.* FROM product p
    #             JOIN product_group pg ON p.id_product_group = pg.id
    #             WHERE pg.commission_percentage >= %s
    return Product.objects.filter(
        product_group__commission_percentage__gte=min_commission,
    )


# =============================================================================
# Q Objects — Queries complexas com OR, AND e NOT
# =============================================================================
# Por padrão, filter() combina condições com AND.
# Para usar OR ou NOT, você PRECISA do objeto Q().
# Operadores: | (OR), & (AND), ~ (NOT)
def get_cheap_or_expensive_products(
    low_price: Decimal,
    high_price: Decimal,
) -> QuerySet[Product]:
    # Q() permite construir queries com OR usando o operador |
    # filter() normal só faz AND — para OR, você PRECISA de Q()
    # Equivale a: SELECT * FROM product
    #             WHERE sale_price < %s OR sale_price > %s
    return Product.objects.filter(
        Q(sale_price__lt=low_price) | Q(sale_price__gt=high_price)
    )


def get_non_male_customers() -> QuerySet[Customer]:
    # ~ inverte o Q(), criando uma condição NOT
    # Equivale a: SELECT * FROM customer WHERE NOT (gender = 'M')
    # Alternativa equivalente: Customer.objects.exclude(gender='M')
    return Customer.objects.filter(~Q(gender="M"))


def get_active_high_income_customers(
    min_income: Decimal,
) -> QuerySet[Customer]:
    # Q() com & faz AND explícito — equivale a dois kwargs no filter()
    # Equivale a: SELECT * FROM customer WHERE active = true AND income >= %s
    # Neste caso, filter(active=True, income__gte=min_income) faria o mesmo
    # Mas & é útil quando combinado com | em expressões maiores
    return Customer.objects.filter(Q(active=True) & Q(income__gte=min_income))


def get_premium_or_female_customers(
    min_income: Decimal,
) -> QuerySet[Customer]:
    # Parênteses controlam a precedência — como em matemática
    # (ativas E renda alta) OU (gênero feminino E ativas)
    # Equivale a: SELECT * FROM customer
    #             WHERE (active = true AND income >= %s)
    #             OR (gender = 'F' AND active = true)
    return Customer.objects.filter(
        (Q(active=True) & Q(income__gte=min_income)) | (Q(gender="F") & Q(active=True))
    )


def get_active_customers_by_name_or_income(
    name_term: str,
    min_income: Decimal,
) -> QuerySet[Customer]:
    # Você pode misturar Q() com kwargs normais no filter()
    # REGRA: Q() deve vir ANTES dos kwargs
    # Equivale a: SELECT * FROM customer
    #             WHERE (name ILIKE '%term%' OR income >= %s)
    #             AND active = true
    return Customer.objects.filter(
        Q(name__icontains=name_term) | Q(income__gte=min_income),
        active=True,  # kwargs normais são combinados com AND ao resultado do Q()
    )


def get_products_matching_any_name(names: list[str]) -> QuerySet[Product]:
    # Q() pode ser construído DINAMICAMENTE em loops
    # Útil quando o número de condições OR varia em tempo de execução
    # Começa com Q() vazio e vai acumulando com |=
    # Equivale a: SELECT * FROM product
    #             WHERE name ILIKE '%nome1%' OR name ILIKE '%nome2%' OR ...
    query = Q()
    for name in names:
        query |= Q(name__icontains=name)
    return Product.objects.filter(query)


def get_employees_complex_filter(
    department_name: str,
    min_salary: Decimal,
    gender: str,
) -> QuerySet[Employee]:
    # Exemplo complexo: combina Q() com lookups de relacionamento
    # (departamento contém termo E salário alto) OU (gênero específico E ativo)
    # Equivale a: SELECT e.* FROM employee e
    #             JOIN department d ON e.id_department = d.id
    #             WHERE (d.name ILIKE '%term%' AND e.salary >= %s)
    #             OR (e.gender = %s AND e.active = true)
    return Employee.objects.filter(
        (Q(department__name__icontains=department_name) & Q(salary__gte=min_salary))
        | (Q(gender=gender) & Q(active=True))
    )


# =============================================================================
# F Expressions — Referenciando valores de campos no banco
# =============================================================================
# F() permite referenciar o valor de um campo do model diretamente no SQL,
# sem trazer o dado para Python. Isso é mais eficiente e evita race conditions.
def get_products_with_positive_margin() -> QuerySet[Product]:
    # F() referencia o valor de um campo NO BANCO — sem trazer para Python
    # Compara dois campos do mesmo registro
    # Equivale a: SELECT * FROM product WHERE sale_price > cost_price
    return Product.objects.filter(sale_price__gt=F("cost_price"))


def get_products_high_margin(min_multiplier: Decimal) -> QuerySet[Product]:
    # F() suporta operações aritméticas: +, -, *, /
    # Aqui: sale_price > cost_price * min_multiplier
    # Se min_multiplier=1.5, busca produtos com margem acima de 50%
    # Equivale a: SELECT * FROM product WHERE sale_price > cost_price * %s
    return Product.objects.filter(
        sale_price__gt=F("cost_price") * min_multiplier,
    )


def increase_all_salaries(percentage: Decimal) -> int:
    # F() permite atualizar usando o valor ATUAL do campo
    # Tudo é feito no banco — NÃO precisa trazer para Python
    # Equivale a: UPDATE employee SET salary = salary * 1.10
    # Exemplo: increase_all_salaries(Decimal('10')) dá aumento de 10%
    # IMPORTANTE: por usar F(), a operação é ATÔMICA — sem race conditions
    multiplier = 1 + percentage / 100
    return Employee.objects.all().update(salary=F("salary") * multiplier)


def apply_discount_to_products(
    discount_percentage: Decimal,
    group_id: int,
) -> int:
    # Aplica desconto em todos os produtos de um grupo
    # F() garante que a operação é atômica — dois requests simultâneos
    # NÃO vão sobrescrever o valor um do outro
    # Equivale a: UPDATE product SET sale_price = sale_price * 0.90
    #             WHERE id_product_group = %s
    multiplier = 1 - discount_percentage / 100
    return Product.objects.filter(
        product_group=group_id,
    ).update(sale_price=F("sale_price") * multiplier)


def get_products_expensive_for_group() -> QuerySet[Product]:
    # F() pode navegar por ForeignKey com '__'
    # Busca produtos cujo preço de venda é maior que o percentual de lucro do grupo * 100
    # Equivale a: SELECT p.* FROM product p
    #             JOIN product_group pg ON p.id_product_group = pg.id
    #             WHERE p.sale_price > pg.gain_percentage * 100
    return Product.objects.filter(
        sale_price__gt=F("product_group__gain_percentage") * 100,
    )


def get_products_where_cost_exceeds_group_commission() -> QuerySet[Product]:
    # Outro exemplo de F() cruzando relacionamento
    # Compara cost_price do produto com commission_percentage do grupo
    # Equivale a: SELECT p.* FROM product p
    #             JOIN product_group pg ON p.id_product_group = pg.id
    #             WHERE p.cost_price > pg.commission_percentage
    return Product.objects.filter(
        cost_price__gt=F("product_group__commission_percentage"),
    )
def get_total_salary_with_alias() -> dict:
    return Employee.objects.aggregate(total=Sum('salary'))

def get_brach_sales(brach_id: int) -> Decimal:
    return Branch.objects.filter(id=brach_id).aggregate(
        total_sale=Sum(
            F(name="sales__sale_items__quantity") * F(name="sales__sale_items__sale_price")
        ),
    )["total_sale"] or Decimal(value="0.00")

def get_departments_with_employee_count() -> QuerySet[Department]:
    return Department.objects.annotate(
        total_emloyees=Count("employee"),
    )

def get_product_id_and_name() -> QuerySet[Product, dict[str, Any]]:
    return Product.objects.values("id", "name")

def get_products_with_rename_fields() -> QuerySet[Product, dict[str, Any]]:
    return Product.objects.values(
        product_id=F(name="id"),
        product_name=F(name="name"),
        group_name=F(name="product_group__name"),
        supplier_name=F(name="supplier__name"),
        price=F(name="sale_price"),
    )

def get_product_count_by_group() -> QuerySet[Product, dict[str, int]]:
    return Product.objects.values("Product__group__name").annotate(
        total_products=Count("id"),
    )

def get_brach_sales(brach_id: int) -> Decimal:
    return Branch.objects.filter(id=brach_id).aggregate(
        total_sale=Sum(
            F(name="sales__sale__items__quantity") * F(name)
        )
    )

