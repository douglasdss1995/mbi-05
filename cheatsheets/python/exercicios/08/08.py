def tipo_triangulo(a, b, c):
    """Determina o tipo de triângulo baseado nos lados"""
    # Verificar se forma um triângulo válido
    # Um triângulo só é valido quando a soma de dois lados deve ser maior que o terceiro lado.
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é triângulo"

    # Verificar o tipo
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

# Testes
print(tipo_triangulo(5, 5, 5))
print(tipo_triangulo(5, 5, 3))
print(tipo_triangulo(3, 4, 5))
print(tipo_triangulo(1, 2, 10))
print(tipo_triangulo(10, 10, 15))
print(tipo_triangulo(7, 8, 9))
