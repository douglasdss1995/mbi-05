def contador_de_letras(texto):
    """Conta todas as letras de uma string e ordena alfabeticamente"""
    # Converter para minúsculas
    texto = texto.lower()

    # Converter para minúsculas e filtrar apenas letras
    letras = [c.lower() for c in texto if c.isalpha()]
    letras = set(letras)

    # Ordenar alfabeticamente
    contagem_ordenada = sorted(letras)

    return contagem_ordenada


# Testes
print(contador_de_letras("Python é legal e Python é poderoso"))
print(contador_de_letras("Olá, mundo! Olá Python."))
print(contador_de_letras(""))
print(contador_de_letras("a a a b b c"))
