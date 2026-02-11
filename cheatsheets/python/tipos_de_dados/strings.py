# Diferentes formas de criar strings
nome = "João"
sobrenome = "Silva"
nome_completo = "João Silva"
idade = 100
salario = 100

# Strings multilinha
descricao = """
Este é um texto
que ocupa múltiplas
linhas.
"""

# Aspas dentro de strings
frase1 = "Ele disse: 'Olá!'"
frase2 = 'Ela respondeu: "Oi!"'
frase3 = "Caminho: C:\\Users\\João"  # Escape com \\

# Formatação de strings (3 formas)

# 1. Concatenação (antiga, evite)
mensagem = "Olá, " + nome + "!"  # "Olá, João!"

# 2. format() (usada no Django templates)
mensagem = f"Olá, {nome}!"  # "Olá, João!"
mensagem = f"Olá, {nome}! Você tem {idade} anos."

# 3. f-strings (RECOMENDADA - Python 3.6+)
mensagem = f"Olá, {nome}!"  # "Olá, João!"
mensagem = f"{nome} tem {idade} anos."
mensagem = f"O salário é R$ {salario:.2f}"  # Formatação com 2 casas decimais

# Operações com strings
texto = "Python é incrível"

# Métodos importantes (usados no Django)
texto.upper()  # "PYTHON É INCRÍVEL"
texto.lower()  # "python é incrível"
texto.title()  # "Python É Incrível"
texto.strip()  # Remove espaços no início e fim
texto.replace("é", "foi")  # "Python foi incrível"
"-".join(["a", "b", "c"])  # "a-b-c"
texto.count("i")  # 2 (número de ocorrências de "i")

texto.split()  # ["Python", "é", "incrível"]
texto.split("i")  # ["Python é ", "ncrível"]

# Verificações
texto.startswith("Python")  # True
texto.endswith("incrível")  # True
len(texto)  # 17 (tamanho)

# Slicing (fatiamento) - MUITO USADO
texto = "Python"
texto[0]  # "P" (primeiro caractere)
texto[-1]  # "n" (último caractere)
texto[0:3]  # "Pyt" (do 0 ao 2)
texto[:3]  # "Pyt" (do início ao 2)
texto[3:]  # "hon" (do 3 até o fim)
texto[-3:]  # "hon" (últimos 3)
texto[::-1]  # "nohtyP" (inverte)
