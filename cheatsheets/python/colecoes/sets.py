# Criando sets
numeros = {1, 2, 3, 4, 5}
frutas = {"maçã", "banana", "laranja"}
vazio = set()  # {} cria dicionário vazio, não set!

# Sets eliminam duplicatas automaticamente
numeros = {1, 2, 3}
print(numeros)  # {1, 2, 3}

# Não tem ordem garantida
frutas = {"maçã", "banana", "laranja"}
# frutas[0]  # ❌ ERRO! Sets não têm índice

# Operações de conjunto
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))  # {1, 2, 3, 4, 5, 6} (união)
print(a | b)  # {1, 2, 3, 4, 5, 6} (mesma coisa)

print(a.intersection(b))  # {3, 4} (interseção)
print(a & b)  # {3, 4} (mesma coisa)

print(a.difference(b))  # {1, 2} (em a mas não em b)
print(a - b)  # {1, 2} (mesma coisa)

# Modificando sets
frutas.add("uva")
frutas.remove("maçã")  # Erro se não existir
frutas.discard("maçã")  # Não dá erro se não existir
frutas.clear()

# Verificando existência (MUITO RÁPIDO!)
numeros = {1, 2, 3, 4, 5}
print(3 in numeros)  # True (mais rápido que em lista)

# Uso prático Django
# Remover IDs duplicados de uma lista
ids = [1, 2, 2, 3, 3, 3, 4]
ids_unicos = list(set(ids))
print(ids_unicos)  # [1, 2, 3, 4]

# Encontrar usuários que estão em dois grupos
grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
em_ambos = grupo_a & grupo_b
print(em_ambos)  # {3, 4}

# Listas de usuários de diferentes sistemas
usuarios_sistema_a = ["ana", "bruno", "carlos", "diana", "eduardo", "diana"]
usuarios_sistema_b = ["carlos", "diana", "fernanda", "gabriel", "helena"]
usuarios_sistema_c = ["diana", "igor", "julia"]

# Convertendo para conjuntos (sets) para operações eficientes
# O método set cria uma colação não ordenada de elementos únicos
set_a = set(usuarios_sistema_a)
set_b = set(usuarios_sistema_b)
set_c = set(usuarios_sistema_c)
