def processar_lista(numeros):
    """Processa uma lista de números e retorna estatísticas"""
    if not numeros:
        return (0, 0, 0)

    soma_pares = sum(n for n in numeros if n % 2 == 0)
    soma_impares = sum(n for n in numeros if n % 2 != 0)
    media = sum(numeros) / len(numeros)

    return (soma_pares, soma_impares, media)

# Testes
print(processar_lista([1, 2, 3, 4, 5, 6]))
print(processar_lista([10, 15, 20, 25]))
print(processar_lista([7]))
print(processar_lista([]))
print(processar_lista([2, 4, 6, 8]))
