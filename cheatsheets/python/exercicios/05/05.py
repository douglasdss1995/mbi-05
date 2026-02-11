def analisar_conjuntos(lista_a, lista_b):
    """Analisa operações entre dois conjuntos"""
    set_a = set(lista_a)
    set_b = set(lista_b)

    return {
        'comuns': set_a & set_b,  # Interseção
        'apenas_a': set_a - set_b,  # Diferença
        'apenas_b': set_b - set_a,  # Diferença
        'todos': set_a | set_b  # União
    }

# Testes
print(analisar_conjuntos([1, 2, 3, 4], [3, 4, 5, 6]))
print(analisar_conjuntos(['a', 'b', 'c'], ['c', 'd', 'e']))
print(analisar_conjuntos([1, 1, 2, 2], [2, 2, 3, 3]))
print(analisar_conjuntos([1, 2, 3], [4, 5, 6]))
