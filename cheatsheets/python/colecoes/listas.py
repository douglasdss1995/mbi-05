# Criando listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misto = [1, "texto", 3.14, True]  # Pode misturar tipos
vazia: list = []

# Acessando elementos (índice começa em 0)
print(frutas[0])  # "maçã"
print(frutas[1])  # "banana"
print(frutas[-1])  # "laranja" (último)
print(frutas[-2])  # "banana" (penúltimo)

# Slicing (fatiamento)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[2:5])  # [2, 3, 4]
print(numeros[:3])  # [0, 1, 2]
print(numeros[5:])  # [5, 6, 7, 8, 9]
print(numeros[::2])  # [0, 2, 4, 6, 8] (pula de 2 em 2)
print(numeros[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (inverte)

# Modificando listas
frutas = ["maçã", "banana"]
frutas.append("laranja")  # ["maçã", "banana", "laranja"]
frutas.insert(1, "uva")  # ["maçã", "uva", "banana", "laranja"]
frutas.remove("banana")  # Remove "banana"
frutas.pop()  # Remove e retorna último elemento
frutas.pop(0)  # Remove e retorna elemento no índice 0
del frutas[0]  # Remove elemento no índice 1
frutas.clear()  # Remove todos os elementos

# Operações úteis
numeros = [3, 1, 4, 1, 5, 9, 2]
print(len(numeros))  # 7 (tamanho)
print(max(numeros))  # 9
print(min(numeros))  # 1
print(sum(numeros))  # 25
print(numeros.count(1))  # 2 (quantas vezes aparece 1)
print(numeros.index(4))  # 2 (índice do elemento 4)
numeros.sort()  # Ordena a lista
numeros.reverse()  # Inverte a ordem
print(sorted(numeros))  # Retorna nova lista ordenada (não altera original)

# Verificando existência
frutas = ["maçã", "banana", "laranja"]
print("banana" in frutas)  # True
print("uva" not in frutas)  # True

# Copiando listas (IMPORTANTE!)
lista1 = [1, 2, 3]
lista2 = lista1  # ❌ Não cria cópia! Ambas apontam para mesma lista
lista3 = lista1.copy()  # ✅ Cria cópia
lista4 = lista1[:]  # ✅ Cria cópia (alternativa)
lista5 = list(lista1)  # ✅ Cria cópia (alternativa)
