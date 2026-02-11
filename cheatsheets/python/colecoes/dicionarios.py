# Criando dicionários
pessoa = {"nome": "João", "idade": 35, "cidade": "Manaus"}

# Diferentes formas de criar
vazio = {}
usando_dict = dict(nome="Maria", idade=28)
de_tuplas = dict([("a", 1), ("b", 2)])

# Acessando valores
print(pessoa["nome"])  # "João"
print(pessoa.get("nome"))  # "João"
print(pessoa.get("email"))  # None (não dá erro)
print(pessoa.get("email", "Não informado"))  # Valor padrão

# Modificando e adicionando
pessoa["idade"] = 36  # Modifica
pessoa["email"] = "d@email.com"  # Adiciona nova chave
pessoa["telefone"] = "92999999999"

# Removendo
del pessoa["telefone"]
email = pessoa.pop("email")  # Remove e retorna valor
pessoa.clear()  # Remove tudo

# Métodos importantes
pessoa = {"nome": "João", "idade": 35, "cidade": "Manaus"}

print(pessoa.keys())  # dict_keys(['nome', 'idade', 'cidade'])
print(pessoa.values())  # dict_values(['João', 35, 'Manaus'])
print(pessoa.items())  # dict_items([('nome', 'João'), ...])

# Verificando existência
print("nome" in pessoa)  # True
print("email" in pessoa)  # False

# Iterando
for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Atualizando múltiplos valores
pessoa.update({"idade": 36, "profissao": "Analista"})

# Dicionário aninhado (muito comum no Django!)
funcionario = {
    "nome": "João",
    "idade": 35,
    "endereco": {"rua": "Av. Constantino Nery", "numero": 123, "cidade": "Manaus"},
    "dependentes": [{"nome": "Filho 1", "idade": 5}, {"nome": "Filho 2", "idade": 3}],
}

# Acessando valores aninhados
print(funcionario["endereco"]["cidade"])  # "Manaus"
print(funcionario["dependentes"][0]["nome"])  # "Filho 1"

# Dict Comprehension
quadrados = {x: x**2 for x in range(5)}
print(quadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Exemplo Django
# Dados de requisição POST
data = {"nome": "João Silva", "email": "douglas@email.com", "departamento": "TI"}

# Serializer trabalha com dicionários
# serializer = FuncionarioSerializer(data=data)

# QuerySet values() retorna lista de dicionários
# usuarios = Usuario.objects.values('id', 'nome', 'email')
# [{'id': 1, 'nome': 'João', 'email': 'd@email.com'}, ...]
