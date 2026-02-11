def gerar_tabuada(numero):
    """Gera a tabuada de um número de 1 a 10"""
    tabuada = []
    for i in range(1, 11):
        tabuada.append(numero * i)
    return tabuada

# Testes
print(gerar_tabuada(5))
print(gerar_tabuada(3))
print(gerar_tabuada(1))
print(gerar_tabuada(7))
print(gerar_tabuada(10))
