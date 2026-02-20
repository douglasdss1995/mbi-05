"""
=============================================================================
EXERCÍCIOS: QuerySets e Lookup Expressions no Django
=============================================================================
Pratique os conceitos aprendidos na aula de QuerySets.
Cada exercício tem um enunciado explicando o problema e uma função
com a resolução comentada.

Tente resolver cada exercício ANTES de olhar a resolução!
Dica: comente a resolução e tente implementar sozinho.

Modelos disponíveis (resumo dos campos principais):
- Product: name, cost_price, sale_price, active, id_product_group, id_supplier
- Employee: name, salary, gender, admission_date, birth_date, active, id_department
- Customer: name, gender, income, active, id_district, id_marital_status
- Department: name, active
- ProductGroup: name, commission_percentage, gain_percentage, active
- Sale: date, active, id_branch, id_customer, id_employee
- SaleItem: quantity, sale_price (nullable), active, id_product, id_sale
- State: name, abbreviation, active
- Supplier: name, legal_document, active
- District: name, active, id_city, id_zone
- City: name, active, id_state
- Zone: name, active
=============================================================================
"""

from decimal import Decimal

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
)
from django.db.models.fields import DecimalField as DecimalFieldType

from core.models import (
    Customer,
    Department,
    Employee,
    Product,
    ProductGroup, Branch,
)


# =============================================================================
# Exercício 1 — Produtos caros e ativos
# =============================================================================
# Retorne todos os produtos ATIVOS cujo preço de venda (sale_price) seja
# maior que R$ 100,00. Ordene pelo preço de venda do maior para o menor.
#
# Conceitos praticados: filter(), __gt, order_by()
# SQL equivalente: SELECT * FROM product
#                  WHERE active = true AND sale_price > 100
#                  ORDER BY sale_price DESC
def get_expensive_active_products() -> QuerySet[Product]:
    return (
        Product.objects
        .filter(
            active=True,
            sale_price__gt=Decimal('100'),
        )
        .order_by('-sale_price')
    )


# =============================================================================
# Exercício 2 — Clientes por inicial do nome e faixa de renda
# =============================================================================
# Retorne todos os clientes cujo nome começa com a letra "M"
# (ignorando maiúsculas/minúsculas)
#
# Conceitos praticados: __istartswith, __range
# SQL equivalente: SELECT * FROM customer
#                  WHERE LOWER(name) LIKE LOWER('m%')
def get_customers_m_mid_income() -> QuerySet[Customer]:
    return Customer.objects.filter(
        name__istartswith='M'
    )


# =============================================================================
# Exercício 3 — Funcionários contratados em um ano com salário baixo
# =============================================================================
# Retorne todos os funcionários contratados no ano de 2020 que ganham
# menos de R$ 3.000,00. Ordene por salário crescente.
#
# Conceitos praticados: __year, __lt, order_by()
# SQL equivalente: SELECT * FROM employee
#                  WHERE EXTRACT(YEAR FROM admission_date) = 1995
#                  AND salary < 3000
#                  ORDER BY salary ASC
def get_low_salary_employees_hired_2020() -> QuerySet[Employee]:
    return (
        Employee.objects
        .filter(
            admission_date__year=1995,
            salary__lt=Decimal('3000'),
        )
        .order_by('salary')
    )


# =============================================================================
# Exercício 4 — Produtos fora da faixa de preço média (Q Objects)
# =============================================================================
# Retorne todos os produtos ATIVOS que custam MENOS de R$ 10,00
# OU MAIS de R$ 500,00. Ou seja, produtos muito baratos ou muito caros,
# excluindo os de preço intermediário.
#
# Conceitos praticados: Q(), operador | (OR), misturar Q() com kwargs
# SQL equivalente: SELECT * FROM product
#                  WHERE (sale_price < 10 OR sale_price > 500)
#                  AND active = true
def get_products_outside_price_range() -> QuerySet[Product]:
    return Product.objects.filter(
        Q(sale_price__lt=Decimal('10')) | Q(sale_price__gt=Decimal('500')),
        active=True,
    )


# =============================================================================
# Exercício 5 — Clientes de um estado específico (Spanning Relationships)
# =============================================================================
# Retorne todos os clientes ativos que moram no estado de São Paulo (sigla 'SP').
# O caminho é: Customer -> District -> City -> State (abbreviation).
#
# Conceitos praticados: lookups em relacionamentos (__), spanning 3 ForeignKeys
# SQL equivalente: SELECT c.* FROM customer c
#                  JOIN district d ON c.id_district = d.id
#                  JOIN city ci ON d.id_city = ci.id
#                  JOIN state s ON ci.id_state = s.id
#                  WHERE s.abbreviation = 'SP' AND c.active = true
def get_active_customers_from_sp() -> QuerySet[Customer]:
    return Customer.objects.filter(
        district__city__state__abbreviation='SP',
        active=True,
    )


# =============================================================================
# Exercício 6 — Produtos com margem mínima de 100% (F Expressions)
# =============================================================================
# Retorne todos os produtos onde o preço de venda é pelo menos o DOBRO
# do preço de custo (margem >= 100%). Ordene pelo nome do produto.
#
# Conceitos praticados: F(), aritmética com F, __gte
# SQL equivalente: SELECT * FROM product
#                  WHERE sale_price >= cost_price * 2
#                  ORDER BY name ASC
def get_products_with_double_margin() -> QuerySet[Product]:
    return (
        Product.objects
        .filter(sale_price__gte=F('cost_price') * 2)
        .order_by('name')
    )


# =============================================================================
# Exercício 7 — Estatísticas salariais por departamento (Aggregate)
# =============================================================================
# Para um departamento específico (recebido por parâmetro), calcule:
# - total: soma de todos os salários
# - media: média dos salários
# - menor: menor salário
# - maior: maior salário
# - quantidade: total de funcionários
# Considere APENAS funcionários ativos.
#
# Conceitos praticados: aggregate(), Sum, Avg, Min, Max, Count, filter()
# SQL equivalente: SELECT SUM(salary) AS total, AVG(salary) AS media,
#                         MIN(salary) AS menor, MAX(salary) AS maior,
#                         COUNT(id) AS quantidade
#                  FROM employee
#                  WHERE id_department = %s AND active = true
def get_department_salary_stats(department_id: int) -> dict:
    return (
        Employee.objects
        .filter(
            department=department_id,
            active=True,
        )
        .aggregate(
            total=Sum('salary'),
            media=Avg('salary'),
            menor=Min('salary'),
            maior=Max('salary'),
            quantidade=Count('id'),
        )
    )


# =============================================================================
# Exercício 8 — Departamentos por número de funcionários (Annotate)
# =============================================================================
# Liste todos os departamentos ativos que possuem 3 ou mais funcionários.
# Inclua a contagem de funcionários em cada departamento.
# Ordene do departamento com mais funcionários para o com menos.
#
# Conceitos praticados: annotate(), Count, filter(), order_by()
# SQL equivalente: SELECT d.*, COUNT(e.id) AS total_funcionarios
#                  FROM department d
#                  LEFT JOIN employee e ON e.id_department = d.id
#                  WHERE d.active = true
#                  GROUP BY d.id
#                  HAVING COUNT(e.id) >= 3
#                  ORDER BY total_funcionarios DESC
def get_active_departments_with_many_employees() -> QuerySet[Department]:
    return (
        Department.objects
        .filter(active=True)
        .annotate(total_funcionarios=Count('employee'))
        .filter(total_funcionarios__gte=3)
        .order_by('-total_funcionarios')
    )


# =============================================================================
# Exercício 9 — Produtos com margem de lucro percentual (ExpressionWrapper)
# =============================================================================
# Calcule o percentual de margem de lucro de cada produto usando a fórmula:
#   margem = ((sale_price - cost_price) / cost_price) * 100
# Retorne apenas produtos com margem acima de 50%.
# Ordene pela margem da maior para a menor.
#
# Conceitos praticados: ExpressionWrapper, F(), annotate(), filter(), order_by()
# SQL equivalente: SELECT *,
#                    ((sale_price - cost_price) / cost_price * 100) AS margem
#                  FROM product
#                  WHERE ((sale_price - cost_price) / cost_price * 100) > 50
#                  ORDER BY margem DESC
def get_products_above_50_percent_margin() -> QuerySet[Product]:
    return (
        Product.objects
        .annotate(
            margem=ExpressionWrapper(
                (F('sale_price') - F('cost_price')) / F('cost_price') * 100,
                output_field=DecimalFieldType(max_digits=10, decimal_places=2),
            ),
        )
        .filter(margem__gt=Decimal('50'))
        .order_by('-margem')
    )


# =============================================================================
# Exercício 10 — Ranking de grupos de produto por lucro potencial
# =============================================================================
# Para cada grupo de produto, calcule:
# - total_produtos: quantidade de produtos no grupo
# - preco_medio: preço de venda médio dos produtos
# - lucro_potencial: soma de (sale_price - cost_price) de todos os produtos
#
# Filtre apenas grupos que tenham mais de 2 produtos.
# Ordene pelo lucro potencial do maior para o menor.
# Retorne apenas os 5 primeiros (top 5).
#
# Conceitos praticados: annotate(), Count, Avg, Sum, F(), filter(), order_by(), slicing
# SQL equivalente: SELECT pg.*,
#                    COUNT(p.id) AS total_produtos,
#                    AVG(p.sale_price) AS preco_medio,
#                    SUM(p.sale_price - p.cost_price) AS lucro_potencial
#                  FROM product_group pg
#                  LEFT JOIN product p ON p.id_product_group = pg.id
#                  GROUP BY pg.id
#                  HAVING COUNT(p.id) > 2
#                  ORDER BY lucro_potencial DESC
#                  LIMIT 5
def get_top_5_product_groups_by_profit() -> QuerySet[ProductGroup]:
    return (
        ProductGroup.objects
        .annotate(
            total_produtos=Count('product'),
            preco_medio=Avg('product__sale_price'),
            lucro_potencial=Sum(
                F('product__sale_price') - F('product__cost_price'),
            ),
        )
        .filter(total_produtos__gt=2)
        .order_by('-lucro_potencial')
        [:5]
    )


"""
Salário Médio por Departamento
Objetivo: Calcular o salário médio dos funcionários de cada departamento.
Enunciado:
Mostre cada departamento com seu salário médio, ordenado do maior para o menor salário.
"""


def average_salary() -> None:
    result = Employee.objects.values('department__name').annotate(
        avg_salary=Avg('salary')
    ).order_by('-avg_salary')

    # Exibir resultado
    for item in result:
        print(f"{item['department__name']}: R$ {item['avg_salary']:,.2f}")


"""
Total de Clientes por Estado
Objetivo: Contar quantos clientes existem em cada estado.
Enunciado:
Liste todos os estados mostrando quantos clientes residem em cada um.
"""


def customers_by_state() -> None:
    result = Customer.objects.values(
        'district__city__state__name',
        'district__city__state__abbreviation'
    ).annotate(
        total_customers=Count('id')
    ).order_by('-total_customers')

    # Exibir resultado
    for item in result:
        state = item['district__city__state__name']
        abbr = item['district__city__state__abbreviation']
        total = item['total_customers']
        print(f"{state} ({abbr}): {total} clientes")


"""
Quantidade de Vendas por Filial
Objetivo: Contar quantas vendas foram realizadas em cada filial.
Enunciado:
Mostre cada filial com o total de vendas realizadas, ordenado do maior para o menor.
"""


def sales_by_branch() -> None:
    # result = Branch.objects.values('name').annotate(
    #     total_sales=Count('sales'),
    #     total_value=Sum(
    #         F("sales__sale_items__quantity") * F("sales__sale_items__sale_price")
    #     ),
    # ).order_by('-total_sales')
    #
    # # Exibir resultado
    # for item in result:
    #     print(f"Filial {item.get('name')}: {item.get('total_sales')} vendas com valor de: {item.get('total_value', 0)}")e
    vendas = Branch.objects.values('name').annotate(
        total_value=Sum(
            F('sales__sale_items__quantity') * F('sales__sale_items__sale_price')
        )
    )

    for item in vendas:
        print(f'Branch: {item.get("name")} - Total value: {item.get("total_value")}')
