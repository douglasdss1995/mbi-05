"""
INVERTER PALAVRAS - EXPLICAÇÃO DETALHADA PARA INICIANTES
=========================================================

O que essa Função Faz?
----------------------
Inverte cada palavra individualmente, mas mantém a ordem das palavras na frase.

Exemplo:
- "Python é incrível" → "nohtyP é levírcni"
  * "Python" vira "nohtyP"
  * "é" continua "é"
  * "incrível" vira "levírcni"

Como a Função Funciona (Passo a Passo)
---------------------------------------

1. DIVIDIR O TEXTO EM PALAVRAS (split()):
   texto.split() quebra a frase em uma lista de palavras separadas por espaços.

   Exemplo: "Olá Mundo" → ["Olá", "Mundo"]

2. CRIAR LISTA VAZIA PARA ARMAZENAR RESULTADOS:
   palavras_invertidas = [] vai guardar cada palavra depois de invertida.

3. LOOP EXTERNO - PERCORRER CADA PALAVRA:
   for palavra in palavras:
   Pega cada palavra da lista, uma por vez.

4. INICIAR STRING VAZIA PARA PALAVRA INVERTIDA:
   palavra_invertida = ""
   Essa variável vai acumular as letras na ordem inversa.

5. LOOP INTERNO - INVERTER A PALAVRA:
   for char in reversed(palavra):

   reversed() inverte a ordem dos caracteres da palavra.

   Exemplo com "Olá":
   - char = 'á': palavra_invertida = "" + "á" = "á"
   - char = 'l': palavra_invertida = "á" + "l" = "ál"
   - char = 'O': palavra_invertida = "ál" + "O" = "álO"

6. ADICIONAR PALAVRA INVERTIDA NA LISTA:
   palavras_invertidas.append(palavra_invertida)
   Guarda a palavra já invertida.

7. JUNTAR TODAS AS PALAVRAS DE VOLTA:
   " ".join(palavras_invertidas)
   Une todas as palavras invertidas com um espaço entre elas.

Conceitos Python Importantes Usados
------------------------------------
1. Método split(): Divide uma string em lista de palavras
2. Método join(): Junta elementos de uma lista em uma string
3. Função reversed(): Inverte a ordem dos elementos
4. Lista vazia []: Para armazenar resultados
5. Loop for aninhado: Um loop dentro de outro
6. Concatenação de strings (+=): Juntar textos
7. Método append(): Adiciona elemento no final da lista

Visualização Passo a Passo
--------------------------
Exemplo: inverter_palavras("Olá Mundo")

Passo 1: palavras = ["Olá", "Mundo"]
Passo 2: palavras_invertidas = []

Primeira iteração (palavra = "Olá"):
  - Loop interno inverte: 'O' 'l' 'á' → "álO"
  - palavras_invertidas = ["álO"]

Segunda iteração (palavra = "Mundo"):
  - Loop interno inverte: 'M' 'u' 'n' 'd' 'o' → "odnuM"
  - palavras_invertidas = ["álO", "odnuM"]

Passo final: " ".join(["álO", "odnuM"]) = "álO odnuM"

Exemplos Práticos
-----------------
"Python é incrível"    → "nohtyP é levírcni"
"Olá Mundo"            → "álO odnuM"
"a"                    → "a"
"um dois três"         → "mu siod sêrt"
"Programação em Python" → "oãçamargorP me nohtyP"
"""


def inverter_palavras(texto):
    """Inverte cada palavra individualmente mantendo a ordem das palavras"""

    # Passo 1: Divide o texto em uma lista de palavras
    # split() separa por espaços em branco
    # Exemplo: "Olá Mundo" → ["Olá", "Mundo"]
    palavras = texto.split()

    # Passo 2: Cria uma lista vazia para guardar as palavras invertidas
    palavras_invertidas = []

    # Passo 3: Percorre cada palavra da lista
    for palavra in palavras:
        # Passo 4: Inicia uma string vazia para construir a palavra invertida
        palavra_invertida = ""

        # Passo 5: Percorre cada caractere da palavra de trás para frente
        # reversed(palavra) inverte a ordem dos caracteres
        # Exemplo: reversed("Olá") → 'á', 'l', 'O'
        for char in reversed(palavra):
            # Adiciona cada caractere ao final da string
            # Isso constrói a palavra invertida letra por letra
            palavra_invertida += char

        # Passo 6: Adiciona a palavra invertida na lista de resultados
        palavras_invertidas.append(palavra_invertida)

    # Passo 7: Junta todas as palavras invertidas com espaços entre elas
    # " ".join() une os elementos da lista separados por espaço
    # Exemplo: ["álO", "odnuM"] → "álO odnuM"
    return " ".join(palavras_invertidas)


# ====== TESTES DA FUNÇÃO ======
print("Teste 1:", inverter_palavras("Python é incrível"))
# Resultado: "nohtyP é levírcni"

print("Teste 2:", inverter_palavras("Olá Mundo"))
# Resultado: "álO odnuM"

print("Teste 3:", inverter_palavras("a"))
# Resultado: "a"

print("Teste 4:", inverter_palavras("um dois três"))
# Resultado: "mu siod sêrt"

print("Teste 5:", inverter_palavras("Programação em Python"))
# Resultado: "oãçamargorP me nohtyP"
