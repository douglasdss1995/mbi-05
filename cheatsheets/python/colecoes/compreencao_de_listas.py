# Forma tradicional
quadrados = []
for x in range(10):
    quadrados.append(x ** 2)
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension (mais pythônico)
quadrados = [x ** 2 for x in range(10)]
print(quadrados)

# Com condição
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Transformando strings
nomes = ["douglas", "maria", "joão"]
nomes_upper = [nome.upper() for nome in nomes]
print(nomes_upper)  # ["DOUGLAS", "MARIA", "JOÃO"]

# Exemplo Django - Serializers frequentemente fazem isso
# emails = [usuario.email for usuario in usuarios]
# ids = [produto.id for produto in produtos if produto.ativo]
