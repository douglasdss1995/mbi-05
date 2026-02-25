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
from typing import Any

from django.db.models import (
    Avg,
    Case,
    Count,
    ExpressionWrapper,
    F,
    IntegerField,
    Max,
    Min,
    Q,
    QuerySet,
    Sum,
    Value,
    When,
)
from django.db.models.fields import CharField
from django.db.models.fields import DecimalField as DecimalFieldType
from django.db.models.functions import ExtractYear

from core.models import (
    Branch,
    Customer,
    Department,
    Employee,
    Product,
    ProductGroup,
    Sale,
    SaleItem,
    State,
    Supplier,
    Zone,
)


# =============================================================================
# all() — Retorna todos os registros da tabela
# =============================================================================
def get_all_products() -> QuerySet[Product]:
    """Retorna todos os produtos da tabela.

    Returns:
        QuerySet[Product]: QuerySet com TODOS os registros da tabela 'product'.
            Nota: o QuerySet é lazy, a query só roda quando você consumir os dados.
            Equivale a: SELECT * FROM product
    """
    return Product.objects.all()


def get_all_employees() -> QuerySet[Employee]:
    """Retorna todos os funcionários cadastrados.

    Returns:
        QuerySet[Employee]: QuerySet com todos os funcionários cadastrados.
            Equivale a: SELECT * FROM employee
    """
    return Employee.objects.all()


def get_all_customers() -> QuerySet[Customer]:
    """Retorna todos os clientes cadastrados.

    Returns:
        QuerySet[Customer]: QuerySet com todos os clientes cadastrados.
            Equivale a: SELECT * FROM customer
    """
    return Customer.objects.all()


# =============================================================================
# get() — Retorna UM ÚNICO objeto que corresponda aos filtros
# =============================================================================
def get_product_by_id(product_id: int) -> Product:
    """Busca um produto pelo ID.

    Args:
        product_id: O ID do produto.

    Returns:
        Product: Exatamente um objeto de produto.
            Equivale a: SELECT * FROM product WHERE id = %s LIMIT 1

    Raises:
        Product.DoesNotExist: Se não encontrar nenhum registro.
        Product.MultipleObjectsReturned: Se encontrar mais de um.
    """
    return Product.objects.get(id=product_id)


def get_employee_by_id(employee_id: int) -> Employee:
    """Busca um funcionário pelo ID.

    Args:
        employee_id: O ID do funcionário.

    Returns:
        Employee: Exatamente um objeto de funcionário.

    Raises:
        Employee.DoesNotExist: Se o ID não existir.
    """
    return Employee.objects.get(id=employee_id)


def get_employee_by_name(name: str) -> Employee:
    """Busca um funcionário pelo nome EXATO.

    Args:
        name: O nome exato do funcionário.

    Returns:
        Employee: Exatamente um objeto de funcionário.

    Raises:
        Employee.MultipleObjectsReturned: Se houver mais de um funcionário com o mesmo nome.

    Note:
        Use get() apenas quando você tem CERTEZA de que o resultado será único.
    """
    return Employee.objects.get(name=name)


def get_customer_by_name(name: str) -> Customer:
    """Busca um cliente pelo nome EXATO.

    Args:
        name: O nome exato do cliente.

    Returns:
        Customer: Exatamente um objeto de cliente.

    Raises:
        Customer.MultipleObjectsReturned: Se houver mais de um cliente com o mesmo nome.

    Note:
        Use get() apenas quando você tem CERTEZA de que o resultado será único.
    """
    return Customer.objects.get(name=name)


# =============================================================================
# filter() — Retorna um QuerySet com os registros que correspondem aos filtros
# =============================================================================
def get_active_employees() -> QuerySet[Employee]:
    """Retorna todos os funcionários ativos.

    Returns:
        QuerySet[Employee]: QuerySet com os registros que CORRESPONDEM ao critério.
            Equivale a: SELECT * FROM employee WHERE active = true
    """
    return Employee.objects.filter(active=True)


def get_employees_by_department(department_id: int) -> QuerySet[Employee]:
    """Filtra funcionários pelo departamento.

    Args:
        department_id: O ID do departamento.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários do departamento especificado.
            Usa a relação ForeignKey. Equivale a: SELECT * FROM employee WHERE id_department = %s
    """
    return Employee.objects.filter(department_id=department_id)


# =============================================================================
# order_by() — Ordena os registros por um ou mais campos
# =============================================================================
def get_products_ordered_by_price() -> QuerySet[Product]:
    """Retorna produtos ordenados pelo preço de venda (crescente).

    Returns:
        QuerySet[Product]: QuerySet ordenado pelo campo sale_price em ordem crescente.
            Equivale a: SELECT * FROM product ORDER BY sale_price ASC
            Para ordem decrescente, use '-' antes do nome do campo: order_by('-sale_price')
    """
    return Product.objects.order_by("sale_price")


# =============================================================================
# create() — Cria e salva um novo registro no banco de dados
# =============================================================================
def create_department(name: str) -> Department:
    """Cria um novo departamento.

    Args:
        name: Nome do departamento.

    Returns:
        Department: O objeto de departamento criado e salvo no banco.
            Equivale a: INSERT INTO department (name) VALUES (%s)
            Nota: create() cria E já salva em uma única operação, diferente de instanciar
            o model e depois chamar .save()
    """
    return Department.objects.create(
        name=name,
    )


def create_zone(name: str) -> Zone:
    """Cria uma nova zona.

    Args:
        name: Nome da zona.

    Returns:
        Zone: O objeto de zona criado e salvo no banco.
            Nota: O objeto retornado já possui o ID gerado pelo banco.
    """
    return Zone.objects.create(
        name=name,
    )


def create_product_group(
    name: str,
    commission_percentage: Decimal,
    gain_percentage: Decimal,
) -> ProductGroup:
    """Cria um novo grupo de produto.

    Args:
        name: Nome do grupo.
        commission_percentage: Percentual de comissão.
        gain_percentage: Percentual de lucro.

    Returns:
        ProductGroup: O objeto de grupo de produto criado e salvo no banco.
            Nota: Todos os campos obrigatórios devem ser informados.
    """
    return ProductGroup.objects.create(
        name=name,
        commission_percentage=commission_percentage,
        gain_percentage=gain_percentage,
    )


def create_state(
    name: str,
    abbreviation: str,
) -> State:
    """Cria um novo estado.

    Args:
        name: Nome do estado.
        abbreviation: Sigla do estado.

    Returns:
        State: O objeto de estado criado e salvo no banco.
            Exemplo: create_state('São Paulo', 'SP')
    """
    return State.objects.create(
        name=name,
        abbreviation=abbreviation,
    )


def create_supplier(
    name: str,
    legal_document: str,
) -> Supplier:
    """Cria um novo fornecedor.

    Args:
        name: Nome do fornecedor.
        legal_document: CNPJ ou CPF do fornecedor.

    Returns:
        Supplier: O objeto de fornecedor criado e salvo no banco.

    Raises:
        IntegrityError: Se tentar criar um fornecedor com legal_document duplicado
            (campo é unique).
    """
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
    """Cria um novo produto.

    Args:
        name: Nome do produto.
        cost_price: Preço de custo.
        sale_price: Preço de venda.
        product_group: Objeto ProductGroup do produto.
        supplier: Objeto Supplier do produto.

    Returns:
        Product: O objeto de produto criado e salvo no banco.
    """
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
    """Desativa todos os produtos.

    Returns:
        int: O número de linhas afetadas.
            Equivale a: UPDATE product SET active = false

    Note:
        update() atualiza TODOS os registros do QuerySet de uma vez.
        IMPORTANTE: update() NÃO chama o método save() do model.
        IMPORTANTE: update() NÃO dispara signals (pre_save, post_save).
    """
    return Product.objects.all().update(active=False)


def update_product_group_commission(group_id: int, new_commission: Decimal) -> int:
    """Atualiza o percentual de comissão de um grupo.

    Args:
        group_id: O ID do grupo de produtos.
        new_commission: O novo percentual de comissão.

    Returns:
        int: O número de linhas afetadas.
            Equivale a: UPDATE product_group SET commission_percentage = %s WHERE id = %s
    """
    return ProductGroup.objects.filter(id=group_id).update(
        commission_percentage=new_commission,
    )


def activate_department_by_id(department_id: int) -> int:
    """Ativa um departamento pelo ID.

    Args:
        department_id: O ID do departamento.

    Returns:
        int: 1 se encontrou e atualizou, 0 se não encontrou.
            Equivale a: UPDATE department SET active = true WHERE id = %s
    """
    return Department.objects.filter(id=department_id).update(active=True)


def update_employee_salary(employee_id: int, new_salary: Decimal) -> int:
    """Atualiza o salário de um funcionário.

    Args:
        employee_id: O ID do funcionário.
        new_salary: O novo salário.

    Returns:
        int: O número de linhas afetadas.
            Equivale a: UPDATE employee SET salary = %s WHERE id = %s
    """
    return Employee.objects.filter(id=employee_id).update(salary=new_salary)


def deactivate_customers_by_gender(gender: str) -> int:
    """Desativa todos os clientes de um gênero específico.

    Args:
        gender: O gênero dos clientes a desativar.

    Returns:
        int: O número de linhas afetadas.
            Equivale a: UPDATE customer SET active = false WHERE gender = %s

    Example:
        deactivate_customers_by_gender('M') desativa todos os clientes masculinos.
    """
    return Customer.objects.filter(gender=gender).update(active=False)


# =============================================================================
# delete() — Remove registros do banco de dados
# =============================================================================
def delete_zone_by_id(zone_id: int) -> tuple:
    """Deleta uma zona pelo ID.

    Args:
        zone_id: O ID da zona a deletar.

    Returns:
        tuple: Uma tupla (total_deletado, {detalhamento_por_model}).
            Exemplo de retorno: (1, {'core.Zone': 1})
            Equivale a: DELETE FROM zone WHERE id = %s

    Raises:
        ProtectedError: Se houver ForeignKey com RESTRICT.
    """
    return Zone.objects.filter(id=zone_id).delete()


def delete_inactive_departments() -> tuple:
    """Deleta todos os departamentos inativos.

    Returns:
        tuple: Uma tupla (total_deletado, {detalhamento_por_model}).
            Equivale a: DELETE FROM department WHERE active = false

    Note:
        delete() em massa NÃO chama o método delete() do model individual.
        delete() em massa NÃO dispara signals (pre_delete, post_delete).
    """
    return Department.objects.filter(active=False).delete()


def delete_single_product(product_id: int) -> tuple:
    """Deleta um produto específico pelo ID.

    Args:
        product_id: O ID do produto a deletar.

    Returns:
        tuple: Uma tupla (total_deletado, {detalhamento_por_model}).

    Note:
        Busca o objeto com get() e chama delete() nele.
        Essa forma DISPARA os signals (pre_delete, post_delete).
        Porém, faz duas queries: uma SELECT + uma DELETE.
    """
    product = Product.objects.get(id=product_id)
    return product.delete()


# =============================================================================
# count() — Conta o número de registros
# =============================================================================
def count_all_products() -> int:
    """Conta o total de produtos.

    Returns:
        int: O número total de registros.
            Equivale a: SELECT COUNT(*) FROM product
            Mais eficiente que len(Product.objects.all()) pois a contagem é feita no banco.
    """
    return Product.objects.count()


def count_active_employees() -> int:
    """Conta funcionários ativos.

    Returns:
        int: O número de funcionários ativos.
            Equivale a: SELECT COUNT(*) FROM employee WHERE active = true
    """
    return Employee.objects.filter(active=True).count()


def count_customers_by_gender(gender: str) -> int:
    """Conta clientes por gênero.

    Args:
        gender: O gênero dos clientes.

    Returns:
        int: O número de clientes com o gênero especificado.
            Equivale a: SELECT COUNT(*) FROM customer WHERE gender = %s

    Example:
        count_customers_by_gender('F') conta todas as clientes femininas.
    """
    return Customer.objects.filter(gender=gender).count()


# =============================================================================
# exists() — Verifica se existe pelo menos um registro
# =============================================================================
def has_any_product() -> bool:
    """Verifica se existe pelo menos um produto.

    Returns:
        bool: True se houver pelo menos um produto, False caso contrário.
            Equivale a: SELECT 1 FROM product LIMIT 1
            Mais eficiente que count() > 0, pois para na primeira ocorrência.
    """
    return Product.objects.exists()


def has_active_employees() -> bool:
    """Verifica se existe funcionário ativo.

    Returns:
        bool: True se houver pelo menos um funcionário ativo, False caso contrário.
            Equivale a: SELECT 1 FROM employee WHERE active = true LIMIT 1
    """
    return Employee.objects.filter(active=True).exists()


def has_customer_with_name(name: str) -> bool:
    """Verifica se existe cliente com um nome específico.

    Args:
        name: O nome do cliente.

    Returns:
        bool: True se existir cliente com o nome especificado, False caso contrário.
            Equivale a: SELECT 1 FROM customer WHERE name = %s LIMIT 1

    Note:
        Útil para validações antes de criar registros.
    """
    return Customer.objects.filter(name=name).exists()


def has_high_income_customers(min_income: Decimal) -> bool:
    """Verifica se existe cliente com renda acima do valor informado.

    Args:
        min_income: A renda mínima.

    Returns:
        bool: True se existir cliente com renda >= min_income, False caso contrário.
            Equivale a: SELECT 1 FROM customer WHERE income >= %s LIMIT 1
            Nota: '__gte' significa 'greater than or equal' (maior ou igual).
    """
    return Customer.objects.filter(income__gte=min_income).exists()


# =============================================================================
# first() — Retorna o primeiro registro do QuerySet (ou None)
# =============================================================================
def get_first_product() -> Product | None:
    """Retorna o primeiro produto.

    Returns:
        Product | None: O PRIMEIRO objeto do QuerySet ou None se estiver vazio.
            Equivale a: SELECT * FROM product ORDER BY ... LIMIT 1
            Nunca lança exceção, ao contrário de get().
            Nota: A ordem depende do 'ordering' definido na Meta do model.
    """
    return Product.objects.first()


def get_first_active_employee() -> Employee | None:
    """Retorna o primeiro funcionário ativo.

    Returns:
        Employee | None: O primeiro funcionário ativo pela ordem padrão do model,
            ou None se não houver nenhum funcionário ativo.
    """
    return Employee.objects.filter(active=True).first()


def get_cheapest_product() -> Product | None:
    """Retorna o produto mais barato.

    Returns:
        Product | None: O produto com o menor preço de venda, ou None se não houver produtos.
            Equivale a: SELECT * FROM product ORDER BY sale_price ASC LIMIT 1

    Note:
        Combina order_by() com first() para pegar o produto mais barato.
        order_by('sale_price') ordena do menor para o maior preço.
        first() pega o primeiro da lista (o mais barato).
    """
    return Product.objects.order_by("sale_price").first()


# =============================================================================
# last() — Retorna o último registro do QuerySet (ou None)
# =============================================================================
def get_last_product() -> Product | None:
    """Retorna o último produto.

    Returns:
        Product | None: O ÚLTIMO objeto do QuerySet ou None se estiver vazio.
            Equivale a: SELECT * FROM product ORDER BY ... DESC LIMIT 1

    Note:
        A ordem depende do 'ordering' definido na Meta do model.
        IMPORTANTE: para funcionar corretamente, o QuerySet deve estar ordenado.
    """
    return Product.objects.last()


def get_last_active_employee() -> Employee | None:
    """Retorna o último funcionário ativo.

    Returns:
        Employee | None: O último funcionário ativo, ou None se não houver nenhum ativo.
    """
    return Employee.objects.filter(active=True).last()


def get_most_expensive_product() -> Product | None:
    """Retorna o produto mais caro.

    Returns:
        Product | None: O produto com o maior preço de venda, ou None se não houver produtos.
            Equivale a: SELECT * FROM product ORDER BY sale_price ASC LIMIT 1 OFFSET (COUNT-1)

    Note:
        Combina order_by() com last() para pegar o produto mais caro.
        order_by('sale_price') ordena do menor para o maior.
        last() pega o último (o mais caro).
        Alternativa mais eficiente: order_by('-sale_price').first()
    """
    return Product.objects.order_by("sale_price").last()


# =============================================================================
# Slicing — Fatiar o QuerySet como uma lista Python
# =============================================================================
def get_first_five_products() -> QuerySet[Product]:
    """Retorna os 5 primeiros produtos.

    Returns:
        QuerySet[Product]: QuerySet com os 5 primeiros registros.
            Equivale a: SELECT * FROM product LIMIT 5

    Note:
        Slicing funciona como em listas Python: [inicio:fim].
        IMPORTANTE: slicing NÃO suporta índices negativos.
    """
    return Product.objects.all()[:5]


def get_products_from_6_to_10() -> QuerySet[Product]:
    """Retorna produtos da posição 6 até 10.

    Returns:
        QuerySet[Product]: QuerySet com os produtos da posição 6 até 10.
            Equivale a: SELECT * FROM product LIMIT 5 OFFSET 5

    Note:
        Útil para implementar paginação manual.
    """
    return Product.objects.all()[5:10]


def get_single_product_by_index(index: int) -> Product:
    """Retorna um produto específico pelo índice.

    Args:
        index: O índice do produto.

    Returns:
        Product: Um único objeto de produto.
            Equivale a: SELECT * FROM product LIMIT 1 OFFSET %s

    Raises:
        IndexError: Se o índice estiver fora do range.
    """
    return Product.objects.all()[index]


def get_first_three_employees_by_salary() -> QuerySet[Employee]:
    """Retorna os 3 funcionários com menor salário.

    Returns:
        QuerySet[Employee]: QuerySet com os 3 funcionários com menor salário.
            Equivale a: SELECT * FROM employee ORDER BY salary ASC LIMIT 3

    Note:
        Combina order_by() com slicing para pegar os 3 funcionários.
        Primeiro ordena por salário crescente, depois fatia os 3 primeiros.
    """
    return Employee.objects.order_by("salary")[:3]


def get_top_three_highest_paid_employees() -> QuerySet[Employee]:
    """Retorna os 3 funcionários com maior salário.

    Returns:
        QuerySet[Employee]: QuerySet com os 3 funcionários com maior salário.
            Equivale a: SELECT * FROM employee ORDER BY salary DESC LIMIT 3

    Note:
        '-salary' ordena do maior para o menor (decrescente).
        [:3] pega os 3 primeiros (os 3 com maior salário).
    """
    return Employee.objects.order_by("-salary")[:3]


# =============================================================================
# Encadeamento de métodos (QuerySet chaining)
# =============================================================================
def get_active_female_customers() -> QuerySet[Customer]:
    """Retorna clientes ativos e femininos.

    Returns:
        QuerySet[Customer]: QuerySet com clientes ativos e femininos.
            Equivale a: SELECT * FROM customer WHERE active = true AND gender = 'F'

    Note:
        QuerySets podem ser ENCADEADOS: cada método retorna um novo QuerySet.
        filter() pode ser chamado múltiplas vezes — os filtros se acumulam com AND.
    """
    return Customer.objects.filter(active=True).filter(gender="F")


def get_active_male_customers_ordered() -> QuerySet[Customer]:
    """Retorna clientes masculinos ativos, ordenados por nome, com limite de 10.

    Returns:
        QuerySet[Customer]: QuerySet com até 10 clientes masculinos ativos, ordenados por nome.
            Equivale a: SELECT * FROM customer WHERE active = true AND gender = 'M'
                        ORDER BY name ASC LIMIT 10

    Note:
        Encadeia filter, order_by e slicing em uma única expressão.
    """
    return Customer.objects.filter(active=True).filter(gender="M").order_by("name")[:10]


# =============================================================================
# BÔNUS — Diferença entre filter() e exclude()
# =============================================================================
def get_active_products() -> QuerySet[Product]:
    """Retorna produtos ativos.

    Returns:
        QuerySet[Product]: QuerySet com registros que CORRESPONDEM ao critério.
            Equivale a: SELECT * FROM product WHERE active = true
    """
    return Product.objects.filter(active=True)


def get_active_products_with_exclude() -> QuerySet[Product]:
    """Retorna produtos ativos usando exclude().

    Returns:
        QuerySet[Product]: QuerySet com registros que NÃO correspondem ao critério.
            Equivale a: SELECT * FROM product WHERE NOT (active = false)

    Note:
        O resultado é o mesmo de filter(active=True), mas a lógica é invertida.
    """
    return Product.objects.exclude(active=False)


# =============================================================================
# Lookups de campo (field lookups)
# =============================================================================
# No Django, lookup expressions são sufixos adicionados ao nome do campo
# usando duplo underscore (__) para definir o TIPO de comparação.
# Sem lookup, o Django assume '__exact' por padrão.
def get_high_salary_employees(min_salary: Decimal) -> QuerySet[Employee]:
    """Retorna funcionários com salário maior ou igual ao especificado.

    Args:
        min_salary: O salário mínimo.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários com salário >= min_salary.
            Equivale a: SELECT * FROM employee WHERE salary >= %s
            Nota: '__gte' = greater than or equal (maior ou igual).
    """
    return Employee.objects.filter(salary__gte=min_salary)


def get_products_by_name_contains(term: str) -> QuerySet[Product]:
    """Retorna produtos cujo nome contém o termo especificado (case-insensitive).

    Args:
        term: O termo a buscar no nome do produto.

    Returns:
        QuerySet[Product]: QuerySet com produtos cujo nome contém o termo.
            Equivale a: SELECT * FROM product WHERE LOWER(name) LIKE LOWER('%term%')
            Nota: '__icontains' = busca case-insensitive (ignora maiúsculas/minúsculas).
    """
    return Product.objects.filter(name__icontains=term)


def get_products_in_price_range(
    min_price: Decimal,
    max_price: Decimal,
) -> QuerySet[Product]:
    """Retorna produtos em uma faixa de preço.

    Args:
        min_price: O preço mínimo.
        max_price: O preço máximo.

    Returns:
        QuerySet[Product]: QuerySet com produtos na faixa de preço especificada.
            Equivale a: SELECT * FROM product WHERE sale_price >= %s AND sale_price <= %s

    Note:
        '__gte' = maior ou igual, '__lte' = menor ou igual.
        Múltiplos filtros no mesmo filter() funcionam como AND.
    """
    return Product.objects.filter(
        sale_price__gte=min_price,
        sale_price__lte=max_price,
    )


def get_employees_name_startswith(prefix: str) -> QuerySet[Employee]:
    """Retorna funcionários cujo nome começa com o prefixo especificado.

    Args:
        prefix: O prefixo do nome.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários cujo nome começa com o prefixo.
            Equivale a: SELECT * FROM employee WHERE LOWER(name) LIKE LOWER('prefix%')
            Nota: '__istartswith' = case-insensitive.
    """
    return Employee.objects.filter(name__istartswith=prefix)


def get_customers_with_income_between(
    min_income: Decimal,
    max_income: Decimal,
) -> QuerySet[Customer]:
    """Retorna clientes com renda em uma faixa específica.

    Args:
        min_income: A renda mínima.
        max_income: A renda máxima.

    Returns:
        QuerySet[Customer]: QuerySet com clientes cuja renda está entre os valores.
            Equivale a: SELECT * FROM customer WHERE income BETWEEN %s AND %s
            Nota: '__range' = entre dois valores (inclusivo nos dois extremos).
    """
    return Customer.objects.filter(income__range=(min_income, max_income))


# =============================================================================
# exact e iexact (correspondência exata)
# =============================================================================
def get_state_by_abbreviation(abbreviation: str) -> QuerySet[State]:
    """Retorna estados pela sigla (busca exata).

    Args:
        abbreviation: A sigla do estado.

    Returns:
        QuerySet[State]: QuerySet com estados que correspondem à sigla.
            Equivale a: SELECT * FROM state WHERE abbreviation = %s

    Note:
        '__exact' é o lookup PADRÃO — você não precisa escrevê-lo.
        State.objects.filter(abbreviation='SP') é idêntico a
        State.objects.filter(abbreviation__exact='SP').
    """
    return State.objects.filter(abbreviation__exact=abbreviation)


def get_customer_by_name_case_insensitive(name: str) -> QuerySet[Customer]:
    """Retorna clientes por nome (busca exata, case-insensitive).

    Args:
        name: O nome do cliente.

    Returns:
        QuerySet[Customer]: QuerySet com clientes cujo nome corresponde exatamente.
            Equivale a: SELECT * FROM customer WHERE LOWER(name) = LOWER(%s)

    Note:
        '__iexact' faz comparação exata, mas IGNORA maiúsculas/minúsculas.
        O 'i' no início significa 'insensitive' (case-insensitive).
        Exemplo: 'joão silva' encontra 'João Silva', 'JOÃO SILVA', etc.
    """
    return Customer.objects.filter(name__iexact=name)


def get_employees_by_gender_exact(gender: str) -> QuerySet[Employee]:
    """Retorna funcionários pelo gênero (busca exata).

    Args:
        gender: O gênero dos funcionários.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários do gênero especificado.
            Equivale a: SELECT * FROM employee WHERE gender = %s

    Note:
        Busca exata por gênero — como é campo curto, exact é o ideal.
    """
    return Employee.objects.filter(gender__exact=gender)


# =============================================================================
# contains e icontains (contém texto)
# =============================================================================
# 'contains' busca texto que CONTENHA o termo (case-sensitive)
# 'icontains' faz o mesmo, mas ignorando maiúsculas/minúsculas
def get_products_name_contains_case_sensitive(term: str) -> QuerySet[Product]:
    """Retorna produtos cujo nome contém o termo (case-sensitive).

    Args:
        term: O termo a buscar.

    Returns:
        QuerySet[Product]: QuerySet com produtos que contêm o termo.
            Equivale a: SELECT * FROM product WHERE name LIKE '%term%'

    Note:
        '__contains' busca CASE-SENSITIVE — 'café' NÃO encontra 'Café'.
        Use quando a diferença entre maiúsculas e minúsculas importa.
    """
    return Product.objects.filter(name__contains=term)


def get_suppliers_name_contains(term: str) -> QuerySet[Supplier]:
    """Retorna fornecedores cujo nome contém o termo (case-insensitive).

    Args:
        term: O termo a buscar.

    Returns:
        QuerySet[Supplier]: QuerySet com fornecedores que contêm o termo.
            Equivale a: SELECT * FROM supplier WHERE LOWER(name) LIKE LOWER('%term%')

    Note:
        '__icontains' busca CASE-INSENSITIVE — 'café' encontra 'Café', 'CAFÉ', etc.
        Na maioria dos casos, icontains é o que você quer para buscas de texto.
    """
    return Supplier.objects.filter(name__icontains=term)


# =============================================================================
# startswith, istartswith, endswith, iendswith
# =============================================================================
# Buscam texto que COMEÇA ou TERMINA com determinado valor
def get_customers_name_startswith(prefix: str) -> QuerySet[Customer]:
    """Retorna clientes cujo nome começa com o prefixo (case-sensitive).

    Args:
        prefix: O prefixo do nome.

    Returns:
        QuerySet[Customer]: QuerySet com clientes que começam com o prefixo.
            Equivale a: SELECT * FROM customer WHERE name LIKE 'prefix%'
    """
    return Customer.objects.filter(name__startswith=prefix)


def get_products_name_endswith(suffix: str) -> QuerySet[Product]:
    """Retorna produtos cujo nome termina com o sufixo (case-sensitive).

    Args:
        suffix: O sufixo do nome.

    Returns:
        QuerySet[Product]: QuerySet com produtos que terminam com o sufixo.
            Equivale a: SELECT * FROM product WHERE name LIKE '%suffix'
    """
    return Product.objects.filter(name__endswith=suffix)


def get_products_name_iendswith(suffix: str) -> QuerySet[Product]:
    """Retorna produtos cujo nome termina com o sufixo (case-insensitive).

    Args:
        suffix: O sufixo do nome.

    Returns:
        QuerySet[Product]: QuerySet com produtos que terminam com o sufixo.
            Equivale a: SELECT * FROM product WHERE LOWER(name) LIKE LOWER('%suffix')

    Example:
        'ml' encontra 'Leite 500ML', 'Suco 1000ml', etc.
    """
    return Product.objects.filter(name__iendswith=suffix)


def get_states_abbreviation_startswith(prefix: str) -> QuerySet[State]:
    """Retorna estados cuja sigla começa com o prefixo especificado.

    Args:
        prefix: O prefixo da sigla.

    Returns:
        QuerySet[State]: QuerySet com estados que começam com o prefixo.
            Equivale a: SELECT * FROM state WHERE abbreviation LIKE 'prefix%'

    Example:
        'S' encontra 'SP', 'SC', 'SE', etc.
    """
    return State.objects.filter(abbreviation__startswith=prefix)


# =============================================================================
# gt e lt (maior que / menor que)
# =============================================================================
# '__gt' = greater than (estritamente maior)
# '__gte' = greater than or equal (maior ou igual)
# '__lt' = less than (estritamente menor)
# '__lte' = less than or equal (menor ou igual)
# Diferente de __gte e __lte que INCLUEM o valor da comparação
def get_products_above_price(price: Decimal) -> QuerySet[Product]:
    """Retorna produtos com preço estritamente maior que o especificado.

    Args:
        price: O preço de referência.

    Returns:
        QuerySet[Product]: QuerySet com produtos acima do preço.
            Equivale a: SELECT * FROM product WHERE sale_price > %s

    Note:
        '__gt' = estritamente MAIOR que (não inclui o valor).
        Se price=100, retorna produtos com preço 100.01 em diante (100 NÃO entra).
    """
    return Product.objects.filter(sale_price__gt=price)


def get_products_at_or_above_price(price: Decimal) -> QuerySet[Product]:
    """Retorna produtos com preço maior ou igual ao especificado.

    Args:
        price: O preço de referência.

    Returns:
        QuerySet[Product]: QuerySet com produtos no preço ou acima.
            Equivale a: SELECT * FROM product WHERE sale_price >= %s

    Note:
        '__gte' = maior ou igual (inclui o valor).
        Se price=100, retorna produtos com preço 100.00 em diante (100 INCLUI).
    """
    return Product.objects.filter(sale_price__gte=price)


def get_products_below_price(price: Decimal) -> QuerySet[Product]:
    """Retorna produtos com preço estritamente menor que o especificado.

    Args:
        price: O preço de referência.

    Returns:
        QuerySet[Product]: QuerySet com produtos abaixo do preço.
            Equivale a: SELECT * FROM product WHERE sale_price < %s

    Note:
        '__lt' = estritamente MENOR que (não inclui o valor).
        Se price=50, retorna produtos com preço até 49.99 (50 NÃO entra).
    """
    return Product.objects.filter(sale_price__lt=price)


def get_products_at_or_below_price(price: Decimal) -> QuerySet[Product]:
    """Retorna produtos com preço menor ou igual ao especificado.

    Args:
        price: O preço de referência.

    Returns:
        QuerySet[Product]: QuerySet com produtos no preço ou abaixo.
            Equivale a: SELECT * FROM product WHERE sale_price <= %s

    Note:
        '__lte' = menor ou igual (inclui o valor).
        Se price=50, retorna produtos com preço até 50.00 (50 INCLUI).
    """
    return Product.objects.filter(sale_price__lte=price)


def get_products_with_profit_margin() -> QuerySet[Product]:
    """Retorna produtos com margem de lucro positiva.

    Returns:
        QuerySet[Product]: QuerySet com produtos onde o preço de venda é maior que o custo.
            Equivale a: SELECT * FROM product WHERE sale_price > cost_price

    Note:
        Usa F() para comparar dois campos do MESMO model.
    """
    return Product.objects.filter(sale_price__gt=F("cost_price"))


def get_employees_salary_below(max_salary: Decimal) -> QuerySet[Employee]:
    """Retorna funcionários com salário menor que o especificado.

    Args:
        max_salary: O salário máximo.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários com salário abaixo do máximo.
            Equivale a: SELECT * FROM employee WHERE salary < %s
    """
    return Employee.objects.filter(salary__lt=max_salary)


# =============================================================================
# in (está na lista)
# =============================================================================
# '__in' verifica se o valor do campo está em uma lista de valores
def get_products_by_ids(product_ids: list[int]) -> QuerySet[Product]:
    """Busca vários produtos pelos IDs.

    Args:
        product_ids: Lista de IDs dos produtos.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem aos IDs.
            Equivale a: SELECT * FROM product WHERE id IN (1, 2, 3, ...)

    Note:
        Mais eficiente que fazer múltiplas chamadas a get().
    """
    return Product.objects.filter(id__in=product_ids)


def get_states_by_abbreviations(abbreviations: list[str]) -> QuerySet[State]:
    """Busca estados por uma lista de siglas.

    Args:
        abbreviations: Lista de siglas dos estados.

    Returns:
        QuerySet[State]: QuerySet com estados que correspondem às siglas.
            Equivale a: SELECT * FROM state WHERE abbreviation IN ('SP', 'RJ', 'MG')

    Example:
        get_states_by_abbreviations(['SP', 'RJ', 'MG'])
    """
    return State.objects.filter(abbreviation__in=abbreviations)


def get_employees_from_departments(department_ids: list[int]) -> QuerySet[Employee]:
    """Busca funcionários de uma lista de departamentos.

    Args:
        department_ids: Lista de IDs dos departamentos.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários dos departamentos especificados.
            Equivale a: SELECT * FROM employee WHERE id_department IN (1, 2, 3)

    Note:
        '__in' também funciona com ForeignKey — filtra pelo ID da relação.
    """
    return Employee.objects.filter(department__in=department_ids)


# =============================================================================
# Lookup Expressions — isnull (campo é nulo)
# =============================================================================
# '__isnull' verifica se o campo é NULL (True) ou NOT NULL (False)
def get_sale_items_without_price() -> QuerySet[SaleItem]:
    """Retorna itens de venda sem preço definido.

    Returns:
        QuerySet[SaleItem]: QuerySet com itens que têm sale_price nulo.
            Equivale a: SELECT * FROM sale_item WHERE sale_price IS NULL

    Note:
        '__isnull=True' filtra registros onde o campo É NULO.
        Útil para encontrar dados incompletos.
    """
    return SaleItem.objects.filter(sale_price__isnull=True)


def get_sale_items_with_price() -> QuerySet[SaleItem]:
    """Retorna itens de venda com preço definido.

    Returns:
        QuerySet[SaleItem]: QuerySet com itens que têm sale_price preenchido.
            Equivale a: SELECT * FROM sale_item WHERE sale_price IS NOT NULL
    """
    return SaleItem.objects.filter(sale_price__isnull=False)


# =============================================================================
# date, year, month, day (lookups temporais)
# =============================================================================
# Lookups para campos DateField e DateTimeField permitem filtrar por
# partes específicas da data
def get_employees_hired_in_year(year: int) -> QuerySet[Employee]:
    """Retorna funcionários contratados em um ano específico.

    Args:
        year: O ano de contratação.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários contratados no ano especificado.
            Equivale a: SELECT * FROM employee WHERE EXTRACT(YEAR FROM admission_date) = %s

    Note:
        '__year' extrai o ANO do campo de data.

    Example:
        get_employees_hired_in_year(2024)
    """
    return Employee.objects.filter(admission_date__year=year)


def get_employees_hired_in_month(month: int) -> QuerySet[Employee]:
    """Retorna funcionários contratados em um mês específico.

    Args:
        month: O mês de contratação (1-12).

    Returns:
        QuerySet[Employee]: QuerySet com funcionários contratados no mês especificado.
            Equivale a: SELECT * FROM employee WHERE EXTRACT(MONTH FROM admission_date) = %s

    Note:
        '__month' extrai o MÊS do campo de data (1-12).

    Example:
        get_employees_hired_in_month(12) — contratados em dezembro.
    """
    return Employee.objects.filter(admission_date__month=month)


def get_employees_born_on_day(day: int) -> QuerySet[Employee]:
    """Retorna funcionários que nasceram em um dia específico do mês.

    Args:
        day: O dia do mês (1-31).

    Returns:
        QuerySet[Employee]: QuerySet com funcionários nascidos no dia especificado.
            Equivale a: SELECT * FROM employee WHERE EXTRACT(DAY FROM birth_date) = %s

    Note:
        '__day' extrai o DIA do campo de data (1-31).

    Example:
        get_employees_born_on_day(25) — nascidos no dia 25.
    """
    return Employee.objects.filter(birth_date__day=day)


def get_employees_hired_in_year_and_month(
    year: int,
    month: int,
) -> QuerySet[Employee]:
    """Retorna funcionários contratados em um ano e mês específicos.

    Args:
        year: O ano de contratação.
        month: O mês de contratação (1-12).

    Returns:
        QuerySet[Employee]: QuerySet com funcionários contratados no período especificado.
            Equivale a: SELECT * FROM employee
                        WHERE EXTRACT(YEAR FROM admission_date) = %s
                        AND EXTRACT(MONTH FROM admission_date) = %s

    Note:
        Podemos ENCADEAR lookups de data para filtrar com precisão.
    """
    return Employee.objects.filter(
        admission_date__year=year,
        admission_date__month=month,
    )


def get_sales_on_date(target_date: date) -> QuerySet[Sale]:
    """Retorna vendas em uma data específica.

    Args:
        target_date: A data alvo.

    Returns:
        QuerySet[Sale]: QuerySet com vendas da data especificada.
            Equivale a: SELECT * FROM sale WHERE DATE(date) = %s

    Note:
        '__date' extrai apenas a parte DATE de um DateTimeField.
        Útil quando o campo é DateTime mas você quer filtrar só pela data.
    """
    return Sale.objects.filter(date__date=target_date)


def get_sales_in_year(year: int) -> QuerySet[Sale]:
    """Retorna vendas de um ano específico.

    Args:
        year: O ano das vendas.

    Returns:
        QuerySet[Sale]: QuerySet com vendas do ano especificado.
            Equivale a: SELECT * FROM sale WHERE EXTRACT(YEAR FROM date) = %s

    Note:
        '__year' funciona tanto em DateField quanto em DateTimeField.
    """
    return Sale.objects.filter(date__year=year)


def get_employees_hired_before_year(year: int) -> QuerySet[Employee]:
    """Retorna funcionários contratados antes de um ano específico.

    Args:
        year: O ano de referência.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários contratados antes do ano especificado.
            Equivale a: SELECT * FROM employee WHERE EXTRACT(YEAR FROM admission_date) < %s

    Note:
        Lookups de data podem ser COMBINADOS com outros lookups!
        '__year__lt' = ano MENOR que o valor informado.
    """
    return Employee.objects.filter(admission_date__year__lt=year)


def get_employees_born_after(ref_date: date) -> QuerySet[Employee]:
    """Retorna funcionários nascidos após uma data específica.

    Args:
        ref_date: A data de referência.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários nascidos após a data especificada.
            Equivale a: SELECT * FROM employee WHERE birth_date > %s

    Note:
        '__gt' funciona diretamente em DateField para comparar datas completas.
    """
    return Employee.objects.filter(birth_date__gt=ref_date)


# =============================================================================
# week_day e week (lookups temporais avançados)
# =============================================================================
def get_employees_hired_on_weekday(weekday: int) -> QuerySet[Employee]:
    """Retorna funcionários contratados em um dia da semana específico.

    Args:
        weekday: O dia da semana (1=Domingo, 2=Segunda, ..., 7=Sábado).

    Returns:
        QuerySet[Employee]: QuerySet com funcionários contratados no dia da semana especificado.
            Equivale a: SELECT * FROM employee WHERE DAYOFWEEK(admission_date) = %s

    Note:
        '__week_day' retorna o dia da semana.
        ATENÇÃO: a contagem começa no Domingo (padrão americano).

    Example:
        get_employees_hired_on_weekday(2) — contratados na segunda-feira.
    """
    return Employee.objects.filter(admission_date__week_day=weekday)


def get_sales_in_week(week: int) -> QuerySet[Sale]:
    """Retorna vendas de uma semana específica do ano.

    Args:
        week: O número da semana ISO (1-52/53).

    Returns:
        QuerySet[Sale]: QuerySet com vendas da semana especificada.
            Equivale a: SELECT * FROM sale WHERE EXTRACT(WEEK FROM date) = %s

    Note:
        '__week' retorna o número da semana ISO do ano (1-52/53).

    Example:
        get_sales_in_week(1) — vendas na primeira semana do ano.
    """
    return Sale.objects.filter(date__week=week)


# =============================================================================
# regex e iregex (expressões regulares)
# =============================================================================
# Permitem buscas usando expressões regulares — mais poderosas que contains
def get_products_name_regex(pattern: str) -> QuerySet[Product]:
    """Busca produtos por expressão regular no nome (case-sensitive).

    Args:
        pattern: O padrão regex a buscar.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao padrão.
            Equivale a: SELECT * FROM product WHERE name ~ 'pattern' (PostgreSQL)

    Note:
        '__regex' faz busca com expressão regular (CASE-SENSITIVE).

    Example:
        get_products_name_regex(r'^[ABC]') — nomes que começam com A, B ou C.
    """
    return Product.objects.filter(name__regex=pattern)


def get_products_name_iregex(pattern: str) -> QuerySet[Product]:
    """Busca produtos por expressão regular no nome (case-insensitive).

    Args:
        pattern: O padrão regex a buscar.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao padrão.
            Equivale a: SELECT * FROM product WHERE name ~* 'pattern' (PostgreSQL)

    Note:
        '__iregex' faz busca com expressão regular (CASE-INSENSITIVE).

    Example:
        get_products_name_iregex(r'leite|suco') — contêm "leite" ou "suco".
    """
    return Product.objects.filter(name__iregex=pattern)


def get_employees_name_matches_pattern(pattern: str) -> QuerySet[Employee]:
    """Busca funcionários por expressão regular no nome.

    Args:
        pattern: O padrão regex a buscar.

    Returns:
        QuerySet[Employee]: QuerySet com funcionários que correspondem ao padrão.

    Note:
        Regex é útil quando contains/startswith não são suficientes.

    Example:
        r'^Maria\\s' encontra "Maria Silva", "Maria Santos"
        mas NÃO encontra "Mariana" (pois exige espaço depois de Maria).
    """
    return Employee.objects.filter(name__iregex=pattern)


def get_suppliers_legal_document_pattern(pattern: str) -> QuerySet[Supplier]:
    """Busca fornecedores por expressão regular no documento legal.

    Args:
        pattern: O padrão regex para validar CNPJ/CPF.

    Returns:
        QuerySet[Supplier]: QuerySet com fornecedores que correspondem ao padrão.

    Note:
        Regex para validar formato de CNPJ/CPF.

    Example:
        r'^\\d{2}\\.\\d{3}\\.\\d{3}' encontra documentos no formato XX.XXX.XXX...
    """
    return Supplier.objects.filter(legal_document__regex=pattern)


# =============================================================================
# Lookups em Relacionamentos (spanning relationships)
# =============================================================================
# O Django permite navegar por ForeignKey usando duplo underscore (__)
# Isso gera JOINs automaticamente no SQL
def get_products_by_supplier_name(supplier_name: str) -> QuerySet[Product]:
    """Busca produtos pelo nome do fornecedor.

    Args:
        supplier_name: O nome do fornecedor (busca parcial, case-insensitive).

    Returns:
        QuerySet[Product]: QuerySet com produtos do fornecedor especificado.
            Equivale a: SELECT p.* FROM product p
                        JOIN supplier s ON p.id_supplier = s.id
                        WHERE LOWER(s.name) LIKE LOWER('%supplier_name%')

    Note:
        Navega do Product para o Supplier pelo campo 'id_supplier'.
        '__name__icontains' acessa o campo 'name' do Supplier.
    """
    return Product.objects.filter(supplier__name__icontains=supplier_name)


def get_products_by_group_name(group_name: str) -> QuerySet[Product]:
    """Busca produtos pelo nome do grupo.

    Args:
        group_name: O nome do grupo de produtos (busca parcial, case-insensitive).

    Returns:
        QuerySet[Product]: QuerySet com produtos do grupo especificado.
            Equivale a: SELECT p.* FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        WHERE LOWER(pg.name) LIKE LOWER('%group_name%')

    Note:
        Navega do Product para o ProductGroup.
    """
    return Product.objects.filter(product_group__name__icontains=group_name)


def get_employees_by_department_name(
    department_name: str,
) -> QuerySet[Employee]:
    """Busca funcionários pelo nome do departamento.

    Args:
        department_name: O nome do departamento (busca parcial, case-insensitive).

    Returns:
        QuerySet[Employee]: QuerySet com funcionários do departamento especificado.
            Equivale a: SELECT e.* FROM employee e
                        JOIN department d ON e.id_department = d.id
                        WHERE LOWER(d.name) LIKE LOWER('%department_name%')
    """
    return Employee.objects.filter(
        department__name__icontains=department_name,
    )


def get_customers_by_city_name(city_name: str) -> QuerySet[Customer]:
    """Busca clientes pelo nome da cidade.

    Args:
        city_name: O nome da cidade (busca parcial, case-insensitive).

    Returns:
        QuerySet[Customer]: QuerySet com clientes da cidade especificada.
            Equivale a: SELECT c.* FROM customer c
                        JOIN district d ON c.id_district = d.id
                        JOIN city ci ON d.id_city = ci.id
                        WHERE LOWER(ci.name) LIKE LOWER('%city_name%')

    Note:
        Navega por MÚLTIPLOS relacionamentos: Customer -> District -> City.
        Cada '__' navega para a próxima tabela.
    """
    return Customer.objects.filter(
        district__city__name__icontains=city_name,
    )


def get_customers_by_state_abbreviation(
    abbreviation: str,
) -> QuerySet[Customer]:
    """Busca clientes pela sigla do estado.

    Args:
        abbreviation: A sigla do estado.

    Returns:
        QuerySet[Customer]: QuerySet com clientes do estado especificado.
            Equivale a: SELECT c.* FROM customer c
                        JOIN district d ON c.id_district = d.id
                        JOIN city ci ON d.id_city = ci.id
                        JOIN state s ON ci.id_state = s.id
                        WHERE s.abbreviation = %s

    Note:
        Navega por TRÊS relacionamentos: Customer -> District -> City -> State.
        Django gera os JOINs automaticamente, não importa a profundidade.
    """
    return Customer.objects.filter(
        district__city__state__abbreviation=abbreviation,
    )


def get_employees_in_zone(zone_name: str) -> QuerySet[Employee]:
    """Busca funcionários pela zona.

    Args:
        zone_name: O nome da zona (busca parcial, case-insensitive).

    Returns:
        QuerySet[Employee]: QuerySet com funcionários da zona especificada.
            Equivale a: SELECT e.* FROM employee e
                        JOIN district d ON e.id_district = d.id
                        JOIN zone z ON d.id_zone = z.id
                        WHERE LOWER(z.name) LIKE LOWER('%zone_name%')

    Note:
        Navega: Employee -> District -> Zone.
    """
    return Employee.objects.filter(
        district__zone__name__icontains=zone_name,
    )


def get_products_by_supplier_active_status(
    is_active: bool,
) -> QuerySet[Product]:
    """Busca produtos pelo status ativo do fornecedor.

    Args:
        is_active: True para produtos de fornecedores ativos, False para inativos.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao status.
            Equivale a: SELECT p.* FROM product p
                        JOIN supplier s ON p.id_supplier = s.id
                        WHERE s.active = %s

    Note:
        Lookup em relacionamento com campo booleano.
    """
    return Product.objects.filter(supplier__active=is_active)


def get_products_by_group_min_commission(
    min_commission: Decimal,
) -> QuerySet[Product]:
    """Busca produtos pelo percentual mínimo de comissão do grupo.

    Args:
        min_commission: O percentual mínimo de comissão.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao critério.
            Equivale a: SELECT p.* FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        WHERE pg.commission_percentage >= %s

    Note:
        Combina lookup de relacionamento com lookup de comparação.
        Navega para ProductGroup e filtra por commission_percentage >= valor.
    """
    return Product.objects.filter(
        product_group__commission_percentage__gte=min_commission,
    )


def get_customer_bought(customer_id: int) -> QuerySet[Product]:
    """Busca produtos comprados por um cliente específico.

    Args:
        customer_id: O ID do cliente.

    Returns:
        QuerySet[Product]: QuerySet com produtos comprados pelo cliente.
            Equivale a: SELECT p.* FROM product p
                        JOIN sale_item si ON p.id = si.id_product
                        JOIN sale s ON si.id_sale = s.id
                        WHERE s.id_customer = %s

    Note:
        Navega por múltiplos relacionamentos: Product -> SaleItem -> Sale -> Customer.
    """
    return Product.objects.filter(
        saleitem__sale__customer__id=customer_id,
    )


# =============================================================================
# Relacionamento Reverso (reverse relationships)
# =============================================================================
def get_sale_total(sale_id: int) -> Decimal:
    """Calcula o valor total de uma venda específica.

    Args:
        sale_id: O ID da venda.

    Returns:
        Decimal: O valor total da venda.
            Equivale a: SELECT SUM(si.quantity * si.sale_price) FROM sale_item si
                        WHERE si.id_sale = %s

    Note:
        Navega: Sale -> SaleItem.
        Usa annotate() para calcular o total da venda.
    """
    return Sale.objects.filter(id=sale_id).aggregate(
        total=Sum(F("sale_items__quantity") * F("sale_items__sale_price"))
    ).get("total") or Decimal("0.00")


def get_branch_sales(branch_id: int) -> Decimal:
    """Busca vendas realizadas por uma filial específica.

    Args:
        branch_id: O ID da filial.

    Returns:
        QuerySet[Sale]: QuerySet com vendas da filial especificada.
            Equivale a: SELECT s.* FROM sale s
                        JOIN employee e ON s.id_employee = e.id
                        WHERE e.id_branch = %s

    Note:
        Navega: Sale -> Employee -> Branch.
    """
    return Branch.objects.filter(id=branch_id).aggregate(
        total_sale=Sum(
            F("sales__sale_items__quantity") * F("sales__sale_items__sale_price")
        ),
    )["total_sale"] or Decimal("0.00")


# =============================================================================
# Q Objects — Queries complexas com OR, AND e NOT
# =============================================================================
# Por padrão, filter() combina condições com AND.
# Para usar OR ou NOT, você PRECISA do objeto Q().
# Operadores: | (OR), & (AND), ~ (NOT)
def get_products_by_name_or_id(term: str) -> QuerySet[Product]:
    """Busca produtos pelo nome OU ID.

    Args:
        term: O termo de busca (pode ser nome ou ID).

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao critério.
            Equivale a: SELECT * FROM product
                        WHERE name ILIKE '%term%' OR id = %s
    """
    return Product.objects.filter(Q(name__icontains=term) | Q(id=term))


def get_customers_by_filters(name: str, city: str | None = None) -> QuerySet[Customer]:
    """Busca clientes pelo nome, e opcionalmente pela cidade. Quando a cidade for fornecida,
    não buscar clientes da Matriz.

    Args:
        name (str): Nome do cliente (busca parcial, case-insensitive)
        city (str): Nome da cidade (busca parcial, case-insensitive)

    Returns:
        QuerySet[Customer]: Clientes que correspondem aos filtros aplicados

    Examples:
        # Busca clientes com "Maria" no nome, independentemente da cidade ou filial
        get_customers_by_filters(name="Maria")

        # Busca clientes com "Maria" no nome, na cidade de "Porto", independentemente da filial
        get_customers_by_filters(name="Maria", city="Porto")
    """
    # Começa com filtro obrigatório pelo nome
    query = Q(name__icontains=name)

    # Adiciona filtro por cidade se fornecido
    if city:
        query &= Q(district__city__name__icontains=city)
        # E garante que não sejam clientes da Matriz (id_district != 1)
        query &= ~Q(district__id=1)

    # Aplica o filtro combinado
    return Customer.objects.filter(query)


# =============================================================================
# F Expressions — Referenciando valores de campos no banco
# =============================================================================
# F() permite referenciar o valor de um campo do model diretamente no SQL,
# sem trazer o dado para Python. Isso é mais eficiente e evita race conditions.
def get_products_with_positive_margin() -> QuerySet[Product]:
    """Retorna produtos com margem de lucro positiva.

    Returns:
        QuerySet[Product]: QuerySet com produtos onde sale_price > cost_price.
            Equivale a: SELECT * FROM product WHERE sale_price > cost_price

    Note:
        F() referencia o valor de um campo NO BANCO — sem trazer para Python.
        Compara dois campos do mesmo registro.
    """
    return Product.objects.filter(sale_price__gt=F("cost_price"))


def get_products_high_margin(min_multiplier: Decimal) -> QuerySet[Product]:
    """Retorna produtos com margem de lucro acima de um multiplicador.

    Args:
        min_multiplier: O multiplicador mínimo da margem (ex: 1.5 para 50% de margem).

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao critério.
            Equivale a: SELECT * FROM product WHERE sale_price > cost_price * %s

    Note:
        F() suporta operações aritméticas: +, -, *, /.
        Se min_multiplier=1.5, busca produtos com margem acima de 50%.
    """
    return Product.objects.filter(
        sale_price__gt=F("cost_price") * min_multiplier,
    )


def increase_all_salaries(percentage: Decimal) -> int:
    """Aumenta o salário de todos os funcionários por um percentual.

    Args:
        percentage: O percentual de aumento (ex: 10 para 10%).

    Returns:
        int: O número de registros atualizados.
            Equivale a: UPDATE employee SET salary = salary * 1.10

    Note:
        F() permite atualizar usando o valor ATUAL do campo.
        Tudo é feito no banco — NÃO precisa trazer para Python.
        IMPORTANTE: por usar F(), a operação é ATÔMICA — sem race conditions.

    Example:
        increase_all_salaries(Decimal('10')) dá aumento de 10%.
    """
    multiplier = 1 + percentage / 100
    return Employee.objects.all().update(salary=F("salary") * multiplier)


def apply_discount_to_products(
    discount_percentage: Decimal,
    group_id: int,
) -> int:
    """Aplica desconto em todos os produtos de um grupo.

    Args:
        discount_percentage: O percentual de desconto (ex: 10 para 10% de desconto).
        group_id: O ID do grupo de produtos.

    Returns:
        int: O número de registros atualizados.
            Equivale a: UPDATE product SET sale_price = sale_price * 0.90
                        WHERE id_product_group = %s

    Note:
        F() garante que a operação é atômica — dois requests simultâneos
        NÃO vão sobrescrever o valor um do outro.
    """
    multiplier = 1 - discount_percentage / 100
    return Product.objects.filter(
        product_group=group_id,
    ).update(sale_price=F("sale_price") * multiplier)


def get_products_expensive_for_group() -> QuerySet[Product]:
    """Busca produtos cujo preço é maior que o ganho do grupo multiplicado por 100.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao critério.
            Equivale a: SELECT p.* FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        WHERE p.sale_price > pg.gain_percentage * 100

    Note:
        F() pode navegar por ForeignKey com '__'.
        Busca produtos cujo preço de venda é maior que o percentual de lucro do grupo * 100.
    """
    return Product.objects.filter(
        sale_price__gt=F("product_group__gain_percentage") * 100,
    )


def get_products_where_cost_exceeds_group_commission() -> QuerySet[Product]:
    """Busca produtos cujo custo excede a comissão do grupo.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao critério.
            Equivale a: SELECT p.* FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        WHERE p.cost_price > pg.commission_percentage

    Note:
        Outro exemplo de F() cruzando relacionamento.
        Compara cost_price do produto com commission_percentage do grupo.
    """
    return Product.objects.filter(
        cost_price__gt=F("product_group__commission_percentage"),
    )


def get_products_where_commission_exceeds_cost() -> QuerySet[Product]:
    """Busca produtos onde a comissão do grupo excede o custo do produto.

    Returns:
        QuerySet[Product]: QuerySet com produtos que correspondem ao critério.
            Equivale a: SELECT p.* FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        WHERE pg.commission_percentage >= pg.gain_percentage

    Note:
        Compara commission_percentage do grupo com o percentual de lucro do produto.
    """
    return Product.objects.filter(
        product_group__commission_percentage__gte=F("gain_percentage"),
    )


# =============================================================================
# Aggregate — Agregações (retorna um dicionário com valores calculados)
# =============================================================================
# aggregate() opera sobre o QuerySet INTEIRO e retorna um DICIONÁRIO.
# Diferente de annotate(), que adiciona campos a CADA objeto.
#
# Sintaxe: .aggregate(campo_alias=Funcao('campo'))
# O nome do campo no resultado é gerado automaticamente: campo__funcao,
# mas pode ser personalizado.
#
# Funções disponíveis: Sum, Avg, Count, Min, Max, StdDev, Variance
# Exemplo: .aggregate(total=Sum('salary')) retorna {'total': ...}
# Sum: soma dos valores
# Avg: média dos valores
# Count: contagem de registros
# Min: valor mínimo
# Max: valor máximo
# StdDev: desvio padrão
# Variance: variância


def get_total_employee_salary() -> dict:
    """Calcula o salário total de todos os funcionários.

    Returns:
        dict: Um dicionário com a soma dos salários.
            Equivale a: SELECT SUM(salary) AS salary__sum FROM employee
            Retorna: {'salary__sum': Decimal('150000.00')}

    Note:
        aggregate() retorna um DICIONÁRIO com valores calculados.
        O nome da chave é gerado automaticamente: campo__função.
    """
    return Employee.objects.aggregate(Sum("salary"))


def get_total_salary_with_alias() -> dict:
    """Calcula o salário total com um nome de alias personalizado.

    Returns:
        dict: Um dicionário com a soma dos salários.
            Equivale a: SELECT SUM(salary) AS total FROM employee
            Retorna: {'total': Decimal('150000.00')}

    Note:
        Use keyword arguments para dar um nome personalizado ao resultado.
    """
    return Employee.objects.aggregate(total=Sum("salary"))


def get_average_product_price() -> dict:
    """Calcula o preço médio de todos os produtos.

    Returns:
        dict: Um dicionário com a média dos preços.
            Equivale a: SELECT AVG(sale_price) AS preco_medio FROM product
            Retorna: {'preco_medio': Decimal('49.90')}

    Note:
        Avg() calcula a MÉDIA dos valores.
    """
    return Product.objects.aggregate(preco_medio=Avg("sale_price"))


def get_salary_stats() -> dict:
    """Calcula estatísticas de salários de todos os funcionários.

    Returns:
        dict: Um dicionário com os salários mínimo, médio e máximo.
            Equivale a: SELECT MIN(salary) AS menor, AVG(salary) AS media, MAX(salary) AS maior FROM employee
            Retorna: {'menor': Decimal('1500.00'), 'media': Decimal('7500.00'), 'maior': Decimal('15000.00')}

    Note:
        Você pode calcular MÚLTIPLOS agregados em uma única query.
    """
    return Employee.objects.aggregate(
        menor=Min("salary"),
        media=Avg("salary"),
        maior=Max("salary"),
    )


def get_customer_stats() -> dict:
    """Calcula estatísticas de clientes: total, renda média e renda máxima.

    Returns:
        dict: Um dicionário com as estatísticas dos clientes.
            Retorna: {'total': 500, 'renda_media': Decimal('3500.00'),
                      'maior_renda': Decimal('50000.00')}

    Note:
        Count() conta registros — combine com outros agregados.
        Tudo resolvido em uma ÚNICA query SQL.
    """
    return Customer.objects.aggregate(
        total=Count("id"),
        renda_media=Avg("income"),
        maior_renda=Max("income"),
    )


def get_active_employee_salary_stats() -> dict:
    """Calcula estatísticas de salários de funcionários ativos.

    Returns:
        dict: Um dicionário com soma, o mínimo, a média e o máximo de salários.
            Equivale a: SELECT  SUM(salary) AS total,
                                MIN(salary) AS minimo,
                                AVG(salary) AS media,
                                MAX(salary) AS maximo
                        FROM employee WHERE active = true

    Note:
        aggregate() pode ser combinado com filter() — agrega só os filtrados.
    """
    return Employee.objects.filter(active=True).aggregate(
        total=Sum("salary"),
        minimo=Min("salary"),
        media=Avg("salary"),
        maximo=Max("salary"),
    )


def get_total_sale_items_value() -> dict:
    """Calcula a soma do preço de venda de todos os itens.

    Returns:
        dict: Um dicionário com a soma total dos preços.
            Equivale a: SELECT SUM(sale_price) AS total FROM sale_item

    Note:
        Sum() pode ser usado em qualquer campo numérico.
    """
    return SaleItem.objects.aggregate(total=Sum("sale_price"))


def get_product_price_stats_by_group(group_id: int) -> dict:
    """Calcula estatísticas de preços de produtos de um grupo específico.

    Args:
        group_id: Identificador do grupo de produtos.

    Returns:
        dict: Um dicionário com estatísticas de preços do grupo.
            Equivale a: SELECT
                                MIN(cost_price) AS menor_custo,
                                AVG(sale_price) AS media,
                                MAX(sale_price) AS maior_venda,
                                COUNT(id) AS quantidade
                        FROM product
                        WHERE
                            id_product_group = %s

    Note:
        Combina filter por grupo + múltiplos agregados em uma única query.
    """
    return Product.objects.filter(product_group=group_id).aggregate(
        menor_custo=Min("cost_price"),
        media=Avg("sale_price"),
        maior_venda=Max("sale_price"),
        quantidade=Count("id"),
    )


# =============================================================================
# Annotate — Anotações (adiciona campos calculados a CADA objeto)
# =============================================================================
# annotate() adiciona um campo calculado a CADA registro do QuerySet.
# O campo anotado pode ser usado em filter(), order_by(), values(), etc.
# Diferente de aggregate() que retorna UM dicionário com totais.
def get_departments_with_employee_count() -> QuerySet[Department]:
    """Retorna departamentos com contagem de funcionários de cada um.

    Returns:
        QuerySet[Department]: QuerySet com departamentos e seu total de funcionários.
            Equivale a: SELECT d.*, COUNT(e.id) AS total_employees
                        FROM department d
                        LEFT JOIN employee e ON e.id_department = d.id
                        GROUP BY d.id

    Note:
        annotate() adiciona um campo calculado a CADA objeto do QuerySet.
        Acesse o valor com: department.total_employees
    """
    return Department.objects.annotate(
        total_employees=Count("employee"),
    )


def get_product_groups_with_total_revenue() -> QuerySet[ProductGroup]:
    """Retorna grupos de produtos com receita total de cada um.

    Returns:
        QuerySet[ProductGroup]: QuerySet com grupos de produtos e receita total.
            Equivale a: SELECT pg.*, SUM(p.sale_price) AS receita_total
                        FROM product_group pg
                        LEFT JOIN product p ON p.id_product_group = pg.id
                        GROUP BY pg.id

    Note:
        Soma o preço de venda de todos os produtos do grupo.
        'product__sale_price' navega pelo relacionamento reverso.
    """
    return ProductGroup.objects.annotate(
        receita_total=Sum("product__sale_price"),
    )


def get_departments_ordered_by_employee_count() -> QuerySet[Department]:
    """Retorna departamentos ordenados por número de funcionários (decrescente).

    Returns:
        QuerySet[Department]: QuerySet com departamentos ordenados por total de funcionários.
            Equivale a: SELECT d.*, COUNT(e.id) AS total
                        FROM department d
                        LEFT JOIN employee e ON e.id_department = d.id
                        GROUP BY d.id
                        ORDER BY total DESC

    Note:
        '-total' = decrescente (o departamento com mais funcionários primeiro).
    """
    return Department.objects.annotate(total=Count("employee")).order_by("-total")


def get_products_with_profit() -> QuerySet[Product]:
    """Retorna produtos com lucro calculado de cada um.

    Returns:
        QuerySet[Product]: QuerySet com produtos e seu lucro calculado.
            Equivale a: SELECT *, (sale_price - cost_price) AS profit FROM product

    Note:
        annotate() com F() cria um campo calculado a partir de outros campos.
        Acesse o valor com: product.profit
    """
    return Product.objects.annotate(
        profit=F("sale_price") - F("cost_price"),
    )


def get_departments_with_avg_salary() -> QuerySet[Department]:
    """Retorna departamentos com salário médio de seus funcionários.

    Returns:
        QuerySet[Department]: QuerySet com departamentos e salário médio.
            Equivale a: SELECT d.*, AVG(e.salary) AS salario_medio
                        FROM department d
                        LEFT JOIN employee e ON e.id_department = d.id
                        GROUP BY d.id

    Note:
        'employee__salary' navega: Department -> Employee -> salary
    """
    return Department.objects.annotate(
        salario_medio=Avg("employee__salary"),
    )


def get_product_groups_with_stats() -> QuerySet[ProductGroup]:
    """Retorna grupos de produtos com múltiplas estatísticas calculadas.

    Returns:
        QuerySet[ProductGroup]: QuerySet com grupos de produtos e suas estatísticas.
            Equivale a: SELECT pg.*,
                          COUNT(p.id) AS total_produtos,
                          AVG(p.sale_price) AS preco_medio,
                          MAX(p.sale_price) AS preco_maximo
                        FROM product_group pg
                        LEFT JOIN product p ON p.id_product_group = pg.id
                        GROUP BY pg.id

    Note:
        Múltiplas anotações na mesma query — tudo resolvido em um único SQL.
    """
    return ProductGroup.objects.annotate(
        total_produtos=Count("product"),
        preco_medio=Avg("product__sale_price"),
        preco_maximo=Max("product__sale_price"),
    )


def get_top_departments_by_salary_budget(limit: int) -> QuerySet[Department]:
    """Retorna os departamentos com maior folha salarial total.

    Args:
        limit: Número máximo de departamentos a retornar.

    Returns:
        QuerySet[Department]: QuerySet com departamentos ordenados por folha salarial.
            Equivale a: SELECT d.*, SUM(e.salary) AS folha_total
                        FROM department d
                        LEFT JOIN employee e ON e.id_department = d.id
                        GROUP BY d.id
                        ORDER BY folha_total DESC
                        LIMIT %s

    Note:
        Combina annotate + order_by + slicing.
    """
    return Department.objects.annotate(folha_total=Sum("employee__salary")).order_by(
        "-folha_total"
    )[:limit]


# =============================================================================
# ExpressionWrapper — Expressões com tipo de saída explícito
# =============================================================================
# ExpressionWrapper é necessário quando o Django NÃO consegue inferir
# automaticamente o tipo do resultado de uma expressão.
# Você deve informar o output_field para que o Django saiba o tipo do resultado.
def get_products_with_profit_margin_percentage() -> QuerySet[Product]:
    """Retorna produtos com percentual de margem de lucro calculado.

    Returns:
        QuerySet[Product]: QuerySet com produtos e seu percentual de margem.
            Equivale a: SELECT *,
                          ((sale_price - cost_price) / cost_price * 100) AS margin_pct
                        FROM product

    Note:
        Calcula o percentual de lucro: (venda - custo) / custo * 100
        Sem ExpressionWrapper, o Django não sabe que o resultado é Decimal.
        Acesse o valor com: product.margin_pct
    """
    return Product.objects.annotate(
        margin_pct=ExpressionWrapper(
            (F("sale_price") - F("cost_price")) / F("cost_price") * 100,
            output_field=DecimalFieldType(max_digits=10, decimal_places=2),
        ),
    )


def get_products_with_absolute_profit() -> QuerySet[Product]:
    """Retorna produtos com lucro absoluto em reais calculado.

    Returns:
        QuerySet[Product]: QuerySet com produtos e seu lucro em reais.
            Equivale a: SELECT *, (sale_price - cost_price) AS lucro FROM product

    Note:
        output_field define o tipo do resultado — decimal com 2 casas.
        Calcula o lucro absoluto em reais de cada produto.
    """
    return Product.objects.annotate(
        lucro=ExpressionWrapper(
            F("sale_price") - F("cost_price"),
            output_field=DecimalFieldType(max_digits=16, decimal_places=2),
        ),
    )


def get_products_with_high_margin(
    min_margin: Decimal,
) -> QuerySet[Product]:
    """Retorna produtos com margem de lucro acima de um limite mínimo.

    Args:
        min_margin: Percentual mínimo de margem de lucro.

    Returns:
        QuerySet[Product]: QuerySet com produtos que atendem o critério de margem.
            Equivale a: SELECT *, ((sale_price - cost_price) / cost_price * 100) AS margin_pct
                        FROM product
                        WHERE ((sale_price - cost_price) / cost_price * 100) >= %s

    Note:
        Combina ExpressionWrapper com filter — filtra pelo valor calculado.
        Primeiro anota com o percentual de margem, depois filtra.
    """
    return Product.objects.annotate(
        margin_pct=ExpressionWrapper(
            (F("sale_price") - F("cost_price")) / F("cost_price") * 100,
            output_field=DecimalFieldType(max_digits=10, decimal_places=2),
        ),
    ).filter(margin_pct__gte=min_margin)


def get_products_with_tax_included(tax_rate: Decimal) -> QuerySet[Product]:
    """Retorna produtos com preço calculado incluindo alíquota de imposto.

    Args:
        tax_rate: Percentual de imposto a ser adicionado ao preço.

    Returns:
        QuerySet[Product]: QuerySet com produtos e preço com imposto incluído.
            Equivale a: SELECT *, sale_price * 1.15 AS price_with_tax FROM product

    Note:
        Value() injeta uma CONSTANTE na expressão SQL.
        Calcula: sale_price * (1 + tax_rate / 100) = preço com imposto
    """
    return Product.objects.annotate(
        price_with_tax=ExpressionWrapper(
            F("sale_price") * (Value(1) + Value(tax_rate) / Value(100)),
            output_field=DecimalFieldType(max_digits=16, decimal_places=2),
        ),
    )


def get_products_margin_vs_group_commission() -> QuerySet[Product]:
    """Retorna produtos com margem de lucro comparada à comissão do grupo.

    Returns:
        QuerySet[Product]: QuerySet com produtos e diferença: margem - comissão.
            Equivale a: SELECT p.*,
                          ((p.sale_price - p.cost_price) / p.cost_price * 100)
                          - pg.commission_percentage AS margin_minus_commission
                        FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id

    Note:
        Compara margem do produto com comissão do grupo.
        Navega pelo relacionamento para acessar commission_percentage.
    """
    return Product.objects.annotate(
        margin_minus_commission=ExpressionWrapper(
            (F("sale_price") - F("cost_price")) / F("cost_price") * 100
            - F("product_group__commission_percentage"),
            output_field=DecimalFieldType(max_digits=10, decimal_places=2),
        ),
    )


def get_products_with_high_margin_ordered(
    min_margin: Decimal,
) -> QuerySet[Product]:
    """Retorna produtos com alta margem de lucro, ordenados decrescentemente.

    Args:
        min_margin: Percentual mínimo de margem de lucro.

    Returns:
        QuerySet[Product]: QuerySet com produtos ordenados por margem decrescente.
            Equivale a: SELECT *, ((sale_price - cost_price) / cost_price * 100) AS margin_pct
                        FROM product
                        WHERE ((sale_price - cost_price) / cost_price * 100) >= %s
                        ORDER BY margin_pct DESC

    Note:
        Exemplo completo: ExpressionWrapper + filter + order_by.
        Calcula margem, filtra por mínimo, e ordena da maior para menor.
    """
    return (
        Product.objects.annotate(
            margin_pct=ExpressionWrapper(
                (F("sale_price") - F("cost_price")) / F("cost_price") * 100,
                output_field=DecimalFieldType(max_digits=10, decimal_places=2),
            ),
        )
        .filter(margin_pct__gte=min_margin)
        .order_by("-margin_pct")
    )


# =============================================================================
# Método .values()
# =============================================================================
# .values() retorna um QuerySet de dicionários, ao invés de objetos do model.
# Útil para retornar apenas campos específicos, ou para serialização.
# Retorna apenas os campos id e name dos produtos
def get_product_id_and_name() -> QuerySet[Product, dict[str, Any]]:
    """Retorna apenas os campos id e name dos produtos.

    Returns:
        QuerySet[Product, dict[str, Any]]: QuerySet de dicionários com os campos id e name dos
            produtos.
            Equivale a: SELECT id, name FROM product

    Examples:
        get_product_id_and_name() retorna:
        [
            {'id': 1, 'name': 'Notebook Dell'},
            {'id': 2, 'name': 'Mouse Logitech'},
            ...
        ]
    """
    return Product.objects.values("id", "name")


# Produtos com nome do grupo e nome do fornecedor
def get_products_with_group_and_supplier() -> QuerySet[Product, dict[str, Any]]:
    """Retorna produtos com nome do grupo e nome do fornecedor.

    Returns:
        QuerySet[Product, dict[str, Any]]: QuerySet de dicionários com os campos id, name,
            product_group__name e supplier__name dos produtos.
            Equivale a: SELECT p.id, p.name, pg.name AS product_group__name,
                        s.name AS supplier__name
                        FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        JOIN supplier s ON p.id_supplier = s.id

    Examples:
        get_products_with_group_and_supplier() retorna:
        [
            {'id': 1, 'name': 'Notebook Dell', 'product_group__name': 'Eletrônicos',
             'supplier__name': 'Dell'},
            {'id': 2, 'name': 'Mouse Logitech', 'product_group__name': 'Periféricos',
             'supplier__name': 'Logitech'},
            ...
        ]
    """
    return Product.objects.values(
        "id",
        "name",
        "product_group__name",
        "supplier__name",
    )


# Renomear campos para nomes mais amigáveis
def get_products_with_renamed_fields() -> QuerySet[Product, dict[str, Any]]:
    """Retorna produtos com campos renomeados para nomes mais amigáveis.

    Returns:
        QuerySet[Product, dict[str, Any]]: QuerySet de dicionários com os campos id, name,
            product_group__name e supplier__name dos produtos, renomeados para
            product_id, product_name, group_name e supplier_name respectivamente.
            Equivale a: SELECT
                            p.id AS product_id,
                            p.name AS product_name,
                            pg.name AS group_name,
                            s.name AS supplier_name,
                            p.sale_price AS price
                        FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        JOIN supplier s ON p.id_supplier = s.id
    Examples:
        get_products_with_renamed_fields() retorna:
        [
            {'product_id': 1, 'product_name': 'Notebook Dell', 'group_name': 'Eletrônicos
                'supplier_name': 'Dell', 'price': Decimal('3500.00')},
                {'product_id': 2, 'product_name': 'Mouse Logitech', 'group_name': 'Periféricos',
                'supplier_name': 'Logitech', 'price': Decimal('150.00')},
            ...
        ]
    """
    return Product.objects.values(
        product_id=F("id"),
        product_name=F("name"),
        group_name=F("product_group__name"),
        supplier_name=F("supplier__name"),
        price=F("sale_price"),
    )


# Total de produtos por grupo
def get_product_count_by_group() -> QuerySet[Product, dict[str, Any]]:
    """Retorna o total de produtos por grupo.

    Returns:
        QuerySet[Product, dict[str, Any]]: QuerySet de dicionários com o nome do grupo e a contagem
            de produtos em cada grupo.
            Equivale a: SELECT pg.name AS product_group__name, COUNT(p.id) AS total_products
                        FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        GROUP BY pg.name

    Examples:
        get_product_count_by_group() retorna:
        [
            {'product_group__name': 'Eletrônicos', 'total_products': 10},
            {'product_group__name': 'Periféricos', 'total_products': 5},
            ...
        ]
    """
    return Product.objects.values("product_group__name").annotate(
        total_products=Count("id"),
    )


def get_product_stats_by_group() -> QuerySet[Product, dict[str, Any]]:
    """Retorna estatísticas de produtos por grupo.

    Returns:
        QuerySet[Product, dict[str, Any]]: QuerySet de dicionários com o nome do grupo e as
            estatísticas de produtos em cada grupo (total, preço médio e custo total).
            Equivale a: SELECT
                            pg.name AS product_group__name,
                            COUNT(p.id) AS total_products,
                            AVG(p.sale_price) AS avg_price,
                            SUM(p.cost_price) AS total_cost
                        FROM product p
                        JOIN product_group pg ON p.id_product_group = pg.id
                        GROUP BY pg.name
    Examples:
        get_product_stats_by_group() retorna:
        [
            {'product_group__name': 'Eletrônicos', 'total_products': 10,
             'avg_price': Decimal('3500.00'), 'total_cost': Decimal('25000.00')},
            {'product_group__name': 'Periféricos', 'total_products': 5,
             'avg_price': Decimal('150.00'), 'total_cost': Decimal('500.00')},
            ...
        ]
    """
    return Product.objects.values("product_group__name").annotate(
        total_products=Count("id"),
        avg_price=Avg("sale_price"),
        total_cost=Sum("cost_price"),
    )


# =============================================================================
# Método .values_list()
# =============================================================================
# .values_list() é similar a .values(), mas retorna TUPLAS ao invés de dicionários.
# Útil para retornar apenas um campo específico, ou para exportação.
def get_product_names_as_list() -> QuerySet[Product, list[str]]:
    """Retorna os nomes dos produtos como uma lista de tuplas.

    Returns:
        QuerySet[Product, list[str]]: QuerySet de tuplas contendo os nomes dos produtos.
            Equivale a: SELECT name FROM product

    Examples:
        get_product_names_as_list() retorna:
        [
            ('Notebook Dell',),
            ('Mouse Logitech',),
            ...
        ]
    """
    return Product.objects.values_list("name", flat=True)


def get_product_id_by_group(product_group_id: int) -> list[int]:
    """Retorna os IDs dos produtos de um grupo específico como uma lista de tuplas.

    Args:
        product_group_id: O ID do grupo de produtos para filtrar.

    Returns:
        QuerySet[Product, list[int]]: QuerySet de tuplas contendo os IDs dos produtos do grupo
            especificado.
            Equivale a: SELECT id FROM product WHERE id_product_group = %s

    Examples:
        get_product_id_by_group(1) retorna:
        [
            (1,),
            (3,),
            ...
        ]
    """
    return list(
        Product.objects.filter(product_group=product_group_id).values_list(
            "id", flat=True
        )
    )


# =============================================================================
# Case/When — Condições IF/ELSE no banco
# =============================================================================
def categorize_employee_age(employee_id: int) -> str:
    """Retorna uma descrição da idade do empresado

    Args:
        employee_id (int): O ID do funcionário para categorizar.

    Returns:
        str: A categoria de idade do funcionário.
    """
    # Categorizar funcionários por faixa etária
    employee = (
        Employee.objects.filter(id=employee_id)
        .annotate(
            # Calcular idade (não podemos usar property diretamente)
            # Usamos a lógica no banco de dados
            current_year=Value(date.today().year, output_field=IntegerField()),
            birth_year=ExtractYear("birth_date"),
            calculated_age=F("current_year") - F("birth_year"),
            # Categorizar por faixa etária
            age_category=Case(
                When(calculated_age__lt=18, then=Value("Menor de Idade")),
                When(calculated_age__lt=25, then=Value("Jovem (18-24)")),
                When(calculated_age__lt=35, then=Value("Adulto Jovem (25-34)")),
                When(calculated_age__lt=50, then=Value("Adulto (35-49)")),
                When(calculated_age__lt=60, then=Value("Adulto Maduro (50-59)")),
                When(calculated_age__gte=60, then=Value("Sênior (60+)")),
                default=Value("Não Informado"),
                output_field=CharField(),
            ),
        )
        .first()
    )

    return employee.age_category if employee else "Funcionário não encontrado"


# =============================================================================
# Exercício 1
# =============================================================================
# Contar quantos produtos existem em cada grupo de produtos.
# Liste todos os grupos de produtos ativos, mostrando o nome do grupo e quantos
# produtos cada um possui.
# Imprima o nome do grupo de produtos e a quantidade de produtos
def exercicio_01() -> None:

    result = (
        Product.objects.filter(product_group__active=True)
        .values(product_group_name=F("product_group__name"))
        .annotate(total=Count("id"))
    )

    for item in result:
        print(
            f"Grupo: {item.get('product_group_name')} - Quantidade: {item.get('total')}"
        )


# =============================================================================
# Exercício 2
# =============================================================================
# Liste os nomes de todos os departamentos ativos e quantidade de funcionários.
# Ordene do departamento com mais funcionários para o com menos.
# Imprima o nome do departamento e quantidade
def exercicio_02() -> None:
    result = (
        Department.objects.filter(active=True)
        .values(department_name=F("name"))
        .annotate(total=Count("employees"))
    )

    for item in result:
        print(
            f"Departamento: {item.get('department_name')} - Quantidade: {item.get('total')}"
        )


# =============================================================================
# Exercício 3
# =============================================================================
# Para um departamento específico (recebido por parâmetro), calcule:
# - total: soma de todos os salários
# - media: média dos salários
# - menor: menor salário
# - maior: maior salário
# - quantidade: total de funcionários
# Considere APENAS funcionários ativos.
# Imprima o nome do departamento e os valores calculados
def exercicio_03(department_id: int) -> None:
    department = Department.objects.get(id=department_id)
    print(f"Departamento: {department.name}")
    result = Employee.objects.filter(
        department=department_id,
        active=True,
    ).aggregate(
        total=Sum("salary"),
        media=Avg("salary"),
        menor=Min("salary"),
        maior=Max("salary"),
        quantidade=Count("id"),
    )

    print(f"total: {result.get('total')}")
    print(f"media: {result.get('media')}")
    print(f"menor: {result.get('menor')}")
    print(f"maior: {result.get('maior')}")
    print(f"quantidade: {result.get('quantidade')}")


# =============================================================================
# Exercício 4
# =============================================================================
# Liste a quantidade de vendas e o valor vendido para cada filial
# Considere APENAS filiais ativas.
# Imprima o nome da filial, quantidade de vendas e valor total vendido
def exercicio_04() -> None:
    result = (
        Branch.objects.filter(active=True)
        .annotate(
            total_vendas=Count("sales"),
            valor_vendido=Sum(
                F("sales__sale_items__quantity") * F("sales__sale_items__sale_price")
            ),
        )
        .order_by("-valor_vendido")
    )

    for item in result:
        print(
            f"Filial: {item.name} - Qtd: {item.total_vendas} - Valor: {item.valor_vendido}"
        )
