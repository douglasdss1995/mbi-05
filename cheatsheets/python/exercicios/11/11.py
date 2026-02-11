def calcular_desconto(valor):
    """Calcula o valor final com desconto baseado no valor da compra"""
    if valor > 1000:
        desconto = 0.20
    elif valor >= 500:
        desconto = 0.15
    elif valor >= 200:
        desconto = 0.10
    elif valor >= 100:
        desconto = 0.05
    else:
        desconto = 0

    valor_final = valor * (1 - desconto)
    return round(valor_final, 2)

# Testes
print(calcular_desconto(1500))
print(calcular_desconto(750))
print(calcular_desconto(250))
print(calcular_desconto(150))
print(calcular_desconto(50))
print(calcular_desconto(1000))
print(calcular_desconto(500))
