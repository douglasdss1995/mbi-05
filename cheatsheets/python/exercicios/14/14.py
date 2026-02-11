"""
SEQUÊNCIA DE FIBONACCI - EXPLICAÇÃO DETALHADA PARA INICIANTES
================================================================

O que é a Sequência de Fibonacci?
----------------------------------
A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Por exemplo:
- 1 = 0 + 1
- 2 = 1 + 1
- 3 = 1 + 2
- 5 = 2 + 3

Como a Função Funciona (Passo a Passo)
---------------------------------------

1. TRATAMENTO PARA NÚMEROS INVÁLIDOS (linhas com if n <= 0):
   Se você pedir 0 ou um número negativo de elementos, a função retorna uma lista vazia [].
   Não faz sentido gerar -5 números Fibonacci!

2. CASO ESPECIAL PARA 1 ELEMENTO (if n == 1):
   Se você pedir apenas 1 número, retorna [0] - o primeiro número da sequência.

3. INICIANDO A SEQUÊNCIA (sequencia = [0, 1]):
   Começamos com os dois primeiros números da sequência de Fibonacci: 0 e 1.
   Estes são os "números base" que usamos para calcular os próximos.

4. GERANDO OS PRÓXIMOS NÚMEROS (o loop for):
   Exemplo com n = 5:
   - i = 2: sequencia[1] + sequencia[0] = 1 + 0 = 1  → [0, 1, 1]
   - i = 3: sequencia[2] + sequencia[1] = 1 + 1 = 2  → [0, 1, 1, 2]
   - i = 4: sequencia[3] + sequencia[2] = 2 + 1 = 3  → [0, 1, 1, 2, 3]

Por que i-1 e i-2?
------------------
Quando estamos na posição i, queremos somar:
- O número ANTERIOR → sequencia[i-1]
- O número DOIS POSIÇÕES ATRÁS → sequencia[i-2]

Isso segue a regra de Fibonacci: cada número é a soma dos dois anteriores!

Conceitos Python Importantes Usados
------------------------------------
1. Função: Bloco de código reutilizável (def fibonacci(n):)
2. Condicional: Toma decisões com if
3. Lista: Estrutura que guarda múltiplos valores [0, 1]
4. Loop for: Repete uma ação várias vezes
5. Indexação: Acessa elementos da lista com sequencia[i-1]
6. Método append(): Adiciona um elemento no final da lista

Exemplos Práticos
-----------------
fibonacci(5)  → [0, 1, 1, 2, 3]
fibonacci(8)  → [0, 1, 1, 2, 3, 5, 8, 13]
fibonacci(1)  → [0]
fibonacci(2)  → [0, 1]
fibonacci(10) → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
fibonacci(0)  → []
"""


def fibonacci(n):
    """Gera os N primeiros números da sequência de Fibonacci"""

    # Passo 1: Se n for 0 ou negativo, retorna lista vazia
    if n <= 0:
        return []

    # Passo 2: Se n for 1, retorna apenas o primeiro número [0]
    if n == 1:
        return [0]

    # Passo 3: Inicia a sequência com os dois primeiros números: 0 e 1
    sequencia = [0, 1]

    # Passo 4: Gera os próximos números da sequência
    # Começa do índice 2 (terceiro número) até n
    for i in range(2, n):
        # Cada número é a soma dos dois anteriores
        # sequencia[i-1] = número anterior
        # sequencia[i-2] = número duas posições atrás
        proximo = sequencia[i-1] + sequencia[i-2]

        # Adiciona o novo número no final da lista
        sequencia.append(proximo)

    # Passo 5: Retorna a lista completa com N números
    return sequencia


# ====== TESTES DA FUNÇÃO ======
print("fibonacci(5)  →", fibonacci(5))   # [0, 1, 1, 2, 3]
print("fibonacci(8)  →", fibonacci(8))   # [0, 1, 1, 2, 3, 5, 8, 13]
print("fibonacci(1)  →", fibonacci(1))   # [0]
print("fibonacci(2)  →", fibonacci(2))   # [0, 1]
print("fibonacci(10) →", fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("fibonacci(0)  →", fibonacci(0))   # []
