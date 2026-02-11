# Criando tuplas
coordenadas = (10, 20)
pessoa = ("João", 35, "Manaus")
singleton = (1,)  # Tupla com um elemento (vírgula obrigatória)
vazia = ()

# Acessando elementos (igual listas)
print(pessoa[0])  # "João"
print(pessoa[-1])  # "Manaus"
print(pessoa[1:3])  # (35, "Manaus")

# Desempacotamento (muito útil!)
nome, idade, cidade = pessoa
print(nome)  # "João"
print(idade)  # 35

# Ignorando valores
nome, _, cidade = pessoa  # Ignora idade

# Tuplas são imutáveis
# pessoa[0] = "João"  # ❌ ERRO! Não pode modificar

# Por que usar tuplas?
# 1. Segurança: dados que não devem mudar
# 2. Performance: mais rápidas que listas
# 3. Podem ser chaves de dicionário
# 4. Django usa muito em choices


# Exemplo Django
class Funcionario(models.Model):
    GENEROS = (  # Tupla de tuplas!
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("NB", "Não-binário"),
    )
    genero = models.CharField(max_length=2, choices=GENEROS)
