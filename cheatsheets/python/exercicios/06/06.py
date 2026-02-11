def formatar_dados(nome, idade, salario):
    """Formata dados pessoais em uma string padronizada"""
    return f"Nome: {nome} | Idade: {idade} anos | Salário: R$ {salario:.2f}"

# Testes
print(formatar_dados("joão silva", 25, 3500))
print(formatar_dados("Maria Santos", 30, 5250.5))
print(formatar_dados("pedro", 18, 1500.99))
print(formatar_dados("Ana Costa", 45, 8000))
