# 🐍 Exercícios Python

---

## 📋 Índice

### 🟢 Básico - Fundamentos

1. [Formatação de Strings](#exercício-6-formatação-de-strings)
2. [Classificador de Notas](#exercício-7-classificador-de-notas)
3. [Gerador de Tabuada](#exercício-12-gerador-de-tabuada)

### 🟡 Intermediário - Estruturas de Dados

4. [Contador de Letras](#exercício-2-contador-de-letras)
5. [Manipulação de Listas](#exercício-3-manipulação-de-listas)
6. [Agenda de Contatos](#exercício-4-agenda-de-contatos)
7. [Operações com Sets](#exercício-5-operações-com-sets)
8. [Inverter String](#exercício-15-inverter-string)

### 🟠 Intermediário/Avançado - Validações e Lógica

9. [Validador de Email](#exercício-1-validador-de-email)
10. [Validador de Senha](#exercício-10-validador-de-senha)
11. [Verificador de Triângulos](#exercício-8-verificador-de-triângulos)
12. [Calculadora de IMC](#exercício-9-calculadora-de-imc)
13. [Calculadora de Descontos](#exercício-11-calculadora-de-descontos)

### 🔴 Avançado - Algoritmos

14. [Números Primos](#exercício-13-números-primos)
15. [Fibonacci](#exercício-14-fibonacci)

---

## 🟢 EXERCÍCIOS BÁSICOS

### Exercício 6: Formatação de Strings

**Nível**: Básico
**Tópicos**: Strings, Métodos de String, Formatação

**Descrição**:

Crie uma função chamada **formatar_dados** que recebe nome, idade e salário e retorna uma string formatada.

**Requisitos**:

- Nome em maiúsculas
- Idade com a palavra "anos"
- Salário formatado com R$ e 2 casas decimais

**Exemplos**:

```python
formatar_dados("joão silva", 25, 3500)
# "Nome: JOÃO SILVA | Idade: 25 anos | Salário: R$ 3500.00"

formatar_dados("Maria Santos", 30, 5250.5)
# "Nome: MARIA SANTOS | Idade: 30 anos | Salário: R$ 5250.50"

formatar_dados("pedro", 18, 1500.99)
# "Nome: PEDRO | Idade: 18 anos | Salário: R$ 1500.99"
```

**Dicas**:

- Use o método `.upper()` para converter strings em maiúsculas
- Use f-strings para formatação: `f"R$ {valor:.2f}"`

---

### Exercício 7: Classificador de Notas

**Nível**: Básico
**Tópicos**: Condicionais, If/Elif/Else

**Descrição**:

Crie uma função chamada **classificar_nota** que recebe uma nota (0-100) e retorna o conceito:

**Regras de Classificação**:

- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59
- "Inválido" para valores fora do intervalo

**Exemplos**:

```python
classificar_nota(95)
# "A"

classificar_nota(82)
# "B"

classificar_nota(59)
# "F"

classificar_nota(105)
# "Inválido"

classificar_nota(-5)
# "Inválido"
```

**Dicas**:

- Valide primeiro se a nota está no intervalo válido (0-100)
- Use estruturas if/elif/else encadeadas

---

### Exercício 12: Gerador de Tabuada

**Nível**: Básico
**Tópicos**: Loops, Listas, Range

**Descrição**:

Crie uma função chamada **gerar_tabuada** que recebe um número e retorna uma lista com a tabuada de 1 a 10.

**Exemplos**:

```python
gerar_tabuada(5)
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

gerar_tabuada(3)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

gerar_tabuada(1)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Dicas**:

- Use `range(1, 11)` para gerar números de 1 a 10
- Multiplique o número base por cada valor do range
- Use list comprehension ou loop for com append

---

## 🟡 EXERCÍCIOS INTERMEDIÁRIOS

### Exercício 2: Contador de Letras

**Nível**: Intermediário
**Tópicos**: Strings, Listas, Ordenação, Métodos de String

**Descrição**:

Receba uma frase e retorne uma lista com todas as letras dessa frase.

**Regras**:

- Ignorar diferenças entre maiúsculas e minúsculas
- Considerar apenas letras, ignorar pontuação e números
- Retornar uma lista ordenada alfabeticamente

**Exemplos**:

```python
contador_de_letras("Python é legal e Python é poderoso")
# ['a', 'd', 'e', 'g', 'h', 'l', 'n', 'o', 'p', 'r', 's', 't', 'y', 'é']

contador_de_letras("Olá, mundo! Olá Python.")
# ['d', 'h', 'l', 'm', 'n', 'o', 'p', 't', 'u', 'y', 'á']

contador_de_letras("")
# []
```

**Dicas**:

- Use o método `.isalpha()` para verificar se é letra
- Use `.lower()` para converter em minúsculas
- Use `set()` para pegar letras únicas
- Use `sorted()` para ordenar alfabeticamente

---

### Exercício 3: Manipulação de Listas

**Nível**: Intermediário
**Tópicos**: Listas, Loops, Tuplas, Operações Matemáticas

**Descrição**:

Crie uma função chamada **processar_lista** que recebe uma lista de números e retorna uma tupla com:

- A soma dos números pares
- A soma dos números ímpares
- A média dos números

**Exemplos**:

```python
processar_lista([1, 2, 3, 4, 5, 6])
# (12, 9, 3.5)

processar_lista([10, 15, 20, 25])
# (30, 40, 17.5)

processar_lista([7])
# (0, 7, 7.0)

processar_lista([])
# (0, 0, 0)
```

**Dicas**:

- Use o operador `%` para verificar se um número é par ou ímpar
- Trate o caso especial de lista vazia para evitar divisão por zero
- Use variáveis acumuladoras para somar pares e ímpares

---

### Exercício 4: Agenda de Contatos

**Nível**: Intermediário
**Tópicos**: Dicionários, Listas, Manipulação de Dados

**Descrição**:

Crie uma função chamada **gerenciar_agenda** que recebe um dicionário de contatos e uma operação, e retorna o resultado.

**Operações disponíveis**:

- 'listar': retorna lista de nomes ordenada
- 'emails': retorna lista de todos os emails

**Exemplos**:

```python
agenda = {
    'João': {'email': 'joao@email.com', 'telefones': ['1111-1111', '2222-2222']},
    'Maria': {'email': 'maria@email.com', 'telefones': ['3333-3333']},
    'Pedro': {'email': 'pedro@email.com', 'telefones': ['4444-4444', '5555-5555', '6666-6666']}
}

gerenciar_agenda(agenda, 'listar')
# ['João', 'Maria', 'Pedro']

gerenciar_agenda(agenda, 'emails')
# ['joao@email.com', 'maria@email.com', 'pedro@email.com']

gerenciar_agenda(agenda, 'buscar')
# 'Pedro'
```

**Dicas**:

- Use `.keys()` para acessar as chaves do dicionário
- Use list comprehension para extrair emails
- Use `sorted()` para ordenar a lista de nomes

---

### Exercício 5: Operações com Sets

**Nível**: Intermediário
**Tópicos**: Sets, Operações de Conjuntos, Dicionários

**Descrição**:

Crie uma função chamada **analisar_conjuntos** que recebe duas listas e retorna um dicionário com:

- 'comuns': elementos presentes em ambas as listas
- 'apenas_a': elementos apenas na primeira lista
- 'apenas_b': elementos apenas na segunda lista
- 'todos': todos os elementos únicos

**Exemplos**:

```python
analisar_conjuntos([1, 2, 3, 4], [3, 4, 5, 6])
# {'comuns': {3, 4}, 'apenas_a': {1, 2}, 'apenas_b': {5, 6}, 'todos': {1, 2, 3, 4, 5, 6}}

analisar_conjuntos(['a', 'b', 'c'], ['c', 'd', 'e'])
# {'comuns': {'c'}, 'apenas_a': {'a', 'b'}, 'apenas_b': {'d', 'e'}, 'todos': {'a', 'b', 'c', 'd', 'e'}}

analisar_conjuntos([1, 1, 2, 2], [2, 2, 3, 3])
# {'comuns': {2}, 'apenas_a': {1}, 'apenas_b': {3}, 'todos': {1, 2, 3}}
```

**Dicas**:

- Converta as listas em sets: `set(lista)`
- Use operadores de conjuntos: `&` (interseção), `-` (diferença), `|` (união)
- Interseção: `set_a & set_b`
- Diferença: `set_a - set_b`
- União: `set_a | set_b`

---

### Exercício 15: Inverter String

**Nível**: Intermediário
**Tópicos**: Strings, Loops, Listas, Métodos de String

**Descrição**:

Crie uma função chamada **inverter_palavras** que recebe uma string e retorna a string com cada palavra invertida, mas mantendo a ordem das palavras.

**Exemplos**:

```python
inverter_palavras("Python é incrível")
# "nohtyP é levírcni"

inverter_palavras("Olá Mundo")
# "álO odnuM"

inverter_palavras("a")
# "a"

inverter_palavras("um dois três")
# "mu siod sêrt"
```

**Dicas**:

- Use `.split()` para separar as palavras
- Use `reversed()` ou slicing `[::-1]` para inverter cada palavra
- Use `.join()` para juntar as palavras de volta

---

## 🟠 EXERCÍCIOS INTERMEDIÁRIOS/AVANÇADOS

### Exercício 1: Validador de Email

**Nível**: Intermediário/Avançado
**Tópicos**: Strings, Validação, Lógica Condicional

**Descrição**:

Crie uma função chamada **validar_email** que recebe uma string e retorna True se o email for válido e False caso contrário.

**Regras de validação**:

- Deve conter exatamente um @
- Deve conter pelo menos um . após o @
- Não pode começar ou terminar com @ ou .
- Deve ter pelo menos 5 caracteres

**Exemplos**:

```python
validar_email("usuario@email.com")  # True
validar_email("usuario@email")      # False
validar_email("@email.com")         # False
validar_email("usuario.email.com")  # False
validar_email("a@b.c")              # True
validar_email("c")                  # False
```

**Dicas**:

- Use o método `.count('@')` para contar quantos @ existem
- Use `.find('@')` para encontrar a posição do @
- Verifique se há um ponto após a posição do @
- Valide os caracteres iniciais e finais

---

### Exercício 10: Validador de Senha

**Nível**: Intermediário/Avançado
**Tópicos**: Strings, Validação, Métodos de String, Tuplas

**Descrição**:

Crie uma função chamada **validar_senha** que recebe uma senha e retorna uma tupla (bool, str) indicando se é válida e a razão de não ser válida.

**Uma senha válida deve**:

- Ter pelo menos 8 caracteres
- Conter pelo menos uma letra maiúscula
- Conter pelo menos uma letra minúscula
- Conter pelo menos um número

**Exemplos**:

```python
validar_senha("Senha123")
# (True, "Senha válida")

validar_senha("senha123")
# (False, "Falta letra maiúscula")

validar_senha("SENHA123")
# (False, "Falta letra minúscula")

validar_senha("SenhaForte")
# (False, "Falta número")

validar_senha("Sen1")
# (False, "Menos de 8 caracteres")
```

**Dicas**:

- Use `.isupper()`, `.islower()`, `.isdigit()` para verificar os caracteres
- Use `any()` com list comprehension para verificar condições
- Retorne uma tupla `(True, "Senha válida")` ou `(False, "razão")`

---

### Exercício 8: Verificador de Triângulos

**Nível**: Intermediário/Avançado
**Tópicos**: Lógica Matemática, Condicionais, Geometria

**Descrição**:

Crie uma função chamada **tipo_triangulo** que recebe três lados e retorna o tipo de triângulo:

**Tipos de Triângulo**:

- "Equilátero": todos os lados iguais
- "Isósceles": dois lados iguais
- "Escaleno": todos os lados diferentes
- "Não é triângulo": quando não forma um triângulo válido

**Lembre-se**: A soma de dois lados deve ser maior que o terceiro lado.

**Conceitos Importantes**:

#### Triângulo Equilátero

- Todos os três lados iguais
- Todos os ângulos internos são iguais (60° cada)
- É o triângulo mais simétrico
- Possui 3 eixos de simetria

#### Triângulo Isósceles

- Dois lados têm a mesma medida (lados congruentes)
- Um lado tem medida diferente (base)
- Dois ângulos são iguais (ângulos da base)
- Possui 1 eixo de simetria

#### Triângulo Escaleno

- Todos os lados têm medidas diferentes
- Todos os ângulos internos são diferentes
- Não possui eixos de simetria

**Exemplos**:

```python
tipo_triangulo(5, 5, 5)
# "Equilátero"

tipo_triangulo(5, 5, 3)
# "Isósceles"

tipo_triangulo(3, 4, 5)
# "Escaleno"

tipo_triangulo(1, 2, 10)
# "Não é triângulo"
```

**Dicas**:

- Primeiro valide se forma um triângulo: `a + b > c` e `a + c > b` e `b + c > a`
- Use comparações para verificar igualdade entre lados
- Conte quantos lados são iguais

---

### Exercício 9: Calculadora de IMC

**Nível**: Intermediário/Avançado
**Tópicos**: Cálculos Matemáticos, Tuplas, Condicionais

**Descrição**:

Crie uma função chamada **calcular_imc** que recebe peso (kg) e altura (m) e retorna uma tupla com o IMC e a classificação:

**Classificações**:

- "Abaixo do peso": IMC < 18.5
- "Peso normal": 18.5 <= IMC < 25
- "Sobrepeso": 25 <= IMC < 30
- "Obesidade": IMC >= 30

**Fórmula**: IMC = peso / (altura²)

**Exemplos**:

```python
calcular_imc(70, 1.75)
# (22.86, "Peso normal")

calcular_imc(50, 1.70)
# (17.3, "Abaixo do peso")

calcular_imc(90, 1.75)
# (29.39, "Sobrepeso")

calcular_imc(100, 1.65)
# (36.73, "Obesidade")
```

**Dicas**:

- Calcule o IMC: `peso / (altura ** 2)`
- Arredonde o IMC para 2 casas decimais: `round(imc, 2)`
- Use if/elif para classificar o IMC
- Retorne uma tupla: `(imc, classificação)`

---

### Exercício 11: Calculadora de Descontos

**Nível**: Intermediário/Avançado
**Tópicos**: Condicionais, Cálculos Matemáticos, Regras de Negócio

**Descrição**:

Crie uma função chamada **calcular_desconto** que recebe o valor da compra e retorna o valor final com desconto:

**Tabela de Descontos**:

- 20% de desconto: compras acima de R$ 1000
- 15% de desconto: compras entre R$ 500 e R$ 1000
- 10% de desconto: compras entre R$ 200 e R$ 500
- 5% de desconto: compras entre R$ 100 e R$ 200
- Sem desconto: compras abaixo de R$ 100

**Exemplos**:

```python
calcular_desconto(1500)
# 1200.0

calcular_desconto(750)
# 637.5

calcular_desconto(250)
# 225.0

calcular_desconto(150)
# 142.5

calcular_desconto(50)
# 50.0
```

**Dicas**:

- Use if/elif para verificar as faixas de valor
- Calcule o desconto: `valor * (1 - percentual_desconto)`
- Exemplo: 20% de desconto = `valor * 0.8`

---

## 🔴 EXERCÍCIOS AVANÇADOS

### Exercício 13: Números Primos

**Nível**: Avançado
**Tópicos**: Algoritmos, Loops, Matemática, Listas

**Descrição**:

Crie uma função chamada **listar_primos** que recebe um número N e retorna uma lista com todos os números primos até N.

**O que é um Número Primo?**

Número Primo é um número natural maior que 1 que possui apenas dois divisores: 1 e ele mesmo.

**Importante**:

- 0 → Não é primo
- 1 → Não é primo
- 2 → É o único número primo par

**Exemplos**:

```python
listar_primos(10)
# [2, 3, 5, 7]

listar_primos(20)
# [2, 3, 5, 7, 11, 13, 17, 19]

listar_primos(5)
# [2, 3, 5]

listar_primos(1)
# []
```

**Dicas**:

- Um número é primo se não é divisível por nenhum número de 2 até ele-1
- Otimização: só precisa testar até a raiz quadrada do número
- Use um loop para verificar cada número de 2 até N
- Use outro loop interno para verificar se o número é primo

**Algoritmo Sugerido**:

```
Para cada número n de 2 até N:
    é_primo = True
    Para cada divisor de 2 até raiz_quadrada(n):
        Se n é divisível por divisor:
            é_primo = False
            pare o loop
    Se é_primo:
        adicione n à lista
```

---

### Exercício 14: Fibonacci

**Nível**: Avançado
**Tópicos**: Algoritmos, Sequências, Listas, Loops

**Descrição**:

Crie uma função chamada **fibonacci** que recebe um número N e retorna uma lista com os N primeiros números da sequência de Fibonacci.

**O que é a Sequência de Fibonacci?**

Sequência de Fibonacci é uma sequência numérica onde cada número é a soma dos dois anteriores.

**História**: Descoberta por Leonardo Fibonacci (matemático italiano, século XIII)

**A Sequência**:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
```

**Padrão**:

- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)

**Exemplos**:

```python
fibonacci(5)
# [0, 1, 1, 2, 3]

fibonacci(8)
# [0, 1, 1, 2, 3, 5, 8, 13]

fibonacci(1)
# [0]

fibonacci(2)
# [0, 1]
```

**Dicas**:

- Comece com uma lista inicial: `[0, 1]`
- Use um loop para gerar os próximos números
- Cada número é a soma dos dois anteriores: `lista[i-1] + lista[i-2]`
- Trate casos especiais: n = 0, n = 1, n = 2

**Algoritmo Sugerido**:

```
Se n <= 0: retorne []
Se n == 1: retorne [0]
Se n == 2: retorne [0, 1]

sequencia = [0, 1]
Para i de 2 até n-1:
    próximo = sequencia[i-1] + sequencia[i-2]
    adicione próximo à sequencia
Retorne sequencia
```

---

## 📚 Recursos Adicionais

### Conceitos Python Importantes

**Métodos de String**:

- `.upper()` / `.lower()` - Conversão de case
- `.split()` - Dividir string em lista
- `.join()` - Juntar lista em string
- `.count()` - Contar ocorrências
- `.find()` - Encontrar posição
- `.isalpha()` / `.isdigit()` - Verificar tipo de caractere

**Estruturas de Dados**:

- Listas: `[1, 2, 3]` - Ordenadas e mutáveis
- Tuplas: `(1, 2, 3)` - Ordenadas e imutáveis
- Sets: `{1, 2, 3}` - Não ordenados, únicos
- Dicionários: `{'chave': 'valor'}` - Pares chave-valor

**Operadores Úteis**:

- `%` - Módulo (resto da divisão)
- `**` - Potenciação
- `//` - Divisão inteira
- `and` / `or` / `not` - Operadores lógicos

**Funções Built-in**:

- `len()` - Tamanho
- `sorted()` - Ordenar
- `sum()` - Somar elementos
- `max()` / `min()` - Máximo / Mínimo
- `any()` / `all()` - Verificações booleanas
- `range()` - Gerar sequências

### Dicas de Estudo

1. **Comece pelos exercícios básicos** e vá progredindo
2. **Tente resolver sem olhar a solução** primeiro
3. **Teste com diferentes casos** incluindo casos extremos
4. **Refatore seu código** depois que funcionar
5. **Compare sua solução** com outras abordagens
6. **Pratique regularmente** - consistência é fundamental

### Próximos Passos

Após completar estes exercícios, você estará pronto para:

- Trabalhar com arquivos e exceções
- Usar bibliotecas externas (NumPy, Pandas)
- Desenvolver aplicações web (Django, Flask)
- Criar scripts de automação
- Explorar ciência de dados e machine learning

---

## 📝 Como Usar Este Guia

1. Escolha um exercício baseado no seu nível
2. Leia a descrição e entenda o problema
3. Tente resolver sem olhar exemplos
4. Compare sua solução com os exemplos fornecidos
5. Teste com casos extremos e diferentes inputs
6. Refatore para melhorar legibilidade e eficiência

---

**Bons estudos e happy coding! 🚀**

_Última atualização: 2026_
