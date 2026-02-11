def listar_primos(n):
    """Lista todos os números primos até N - Versão Simples"""

    primos = []  # Lista vazia para guardar os primos

    # Testar cada número de 2 até n
    for numero in range(2, n + 1):

        # Assume que o número é primo
        eh_primo = True

        # Testar se o número é divisível por algum outro número
        for divisor in range(2, numero):
            if numero % divisor == 0:
                # Encontrou um divisor! Não é primo
                eh_primo = False
                break  # Para de testar, já sabemos que não é primo

        # Se passou por todos os testes, é primo!
        if eh_primo:
            primos.append(numero)

    return primos

# Testes
print(listar_primos(10))
print(listar_primos(20))
print(listar_primos(5))
print(listar_primos(1))
print(listar_primos(30))
print(listar_primos(100))
