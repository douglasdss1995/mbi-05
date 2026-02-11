def calcular_imc(peso, altura):
    """Calcula o IMC e retorna a classificação"""
    imc = peso / (altura ** 2)
    imc_formatado = round(imc, 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return (imc_formatado, classificacao)

# Testes
print(calcular_imc(70, 1.75))
print(calcular_imc(50, 1.70))
print(calcular_imc(90, 1.75))
print(calcular_imc(100, 1.65))
print(calcular_imc(60, 1.60))
