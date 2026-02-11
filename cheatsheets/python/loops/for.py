# For básico com lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# For com range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (pula de 2 em 2)
    print(i)

# For com índice usando enumerate
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
# 0: maçã
# 1: banana
# 2: laranja

# For com dicionário
pessoa = {"nome": "João", "idade": 35, "cidade": "Manaus"}

# Apenas chaves
for chave in pessoa:
    print(chave)

# Chave e valor
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Apenas valores
for valor in pessoa.values():
    print(valor)

# For com múltiplas listas (zip)
nomes = ["João", "Maria", "João"]
idades = [35, 28, 42]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# Break - interrompe o loop
for i in range(10):
    if i == 5:
        break  # Para quando i = 5
    print(i)  # 0, 1, 2, 3, 4

# Continue - pula para próxima iteração
for i in range(10):
    if i % 2 == 0:
        continue  # Pula números pares
    print(i)  # 1, 3, 5, 7, 9

# Else com for (executado se não houver break)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completou sem break")
