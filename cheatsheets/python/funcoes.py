# Função simples
def saudacao():
    print("Olá, mundo!")


saudacao()  # Chama a função


# Função com parâmetros
def saudar_pessoa(nome):
    print(f"Olá, {nome}!")


saudar_pessoa("João")  # "Olá, João!"


# Função com múltiplos parâmetros
def somar(a, b):
    resultado = a + b
    return resultado


total = somar(5, 3)  # 8


# Parâmetros com valores padrão
def saudar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"


print(saudar("João"))  # "Olá, João!"
print(saudar("Maria", "Bem-vinda"))  # "Bem-vinda, Maria!"


# Argumentos nomeados
def criar_usuario(nome, email, idade):
    return {"nome": nome, "email": email, "idade": idade}


# Ordem importa
usuario1 = criar_usuario("João", "d@email.com", 35)

# Com argumentos nomeados, ordem não importa
usuario2 = criar_usuario(idade=28, nome="Maria", email="m@email.com")


# Retornando múltiplos valores
def dividir_com_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto  # Retorna tupla


resultado, resto = dividir_com_resto(10, 3)
print(resultado)  # 3
print(resto)  # 1


# Função sem retorno explícito retorna None
def imprimir_algo():
    print("Algo")
    # Sem return


resultado = imprimir_algo()  # None


# *args - número variável de argumentos posicionais
def somar_varios(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total


print(somar_varios(1, 2, 3))  # 6
print(somar_varios(1, 2, 3, 4, 5))  # 15


# **kwargs - número variável de argumentos nomeados
def criar_pessoa(**dados):
    pessoa = {}
    for chave, valor in dados.items():
        pessoa[chave] = valor
    return pessoa


pessoa1 = criar_pessoa(nome="João", idade=35)
pessoa2 = criar_pessoa(nome="Maria", idade=28, cidade="Manaus", profissao="Dev")


# Combinando tudo
def funcao_completa(arg1, arg2, *args, kwarg1="padrão", **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")


funcao_completa(1, 2, 3, 4, 5, kwarg1="valor", extra="teste")


# Exemplo Django
def validar_cpf(cpf):
    """Valida CPF brasileiro"""
    # Remove caracteres não numéricos
    cpf_limpo = "".join(filter(str.isdigit, cpf))

    if len(cpf_limpo) != 11:
        return False

    # Validação simplificada (na prática, use biblioteca)
    return True


def calcular_salario_liquido(salario_bruto, descontos=0):
    """Calcula salário líquido"""
    return salario_bruto - descontos


def criar_funcionario(nome, email, **dados_adicionais):
    """Cria funcionário com dados flexíveis"""
    funcionario = {
        "nome": nome,
        "email": email,
        **dados_adicionais,  # Desempacota dados extras
    }
    # return Funcionario.objects.create(**funcionario)


# Uso
criar_funcionario(
    nome="João", email="d@email.com", departamento="TI", salario=5500.00, ativo=True
)
