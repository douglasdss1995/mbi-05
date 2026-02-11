import time

# While básico
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Importante! Senão loop infinito

# While com break
contador = 0
while True:  # Loop infinito
    print(contador)
    contador += 1
    if contador >= 5:
        break  # Sai do loop

# While com continue
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Pula pares
    print(contador)  # Imprime ímpares

# While com else
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop completou normalmente")

# Exemplo prático - menu
while True:
    print("\n1. Cadastrar")
    print("2. Listar")
    print("3. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        print("Cadastrando...")
    elif opcao == "2":
        print("Listando...")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

# Exemplo Django - Retry pattern
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
        # Tenta conectar ao banco
        # connection.ensure_connection()
        break  # Sucesso, sai do loop
    except Exception:
        tentativas += 1
        if tentativas >= max_tentativas:
            raise Exception("Falha após 3 tentativas")
        time.sleep(2)  # Aguarda 2 segundos antes de tentar novamente
