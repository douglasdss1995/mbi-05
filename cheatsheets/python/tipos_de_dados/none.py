# None representa "nenhum valor" ou "valor nulo"
resultado = None

# Usado quando uma variável ainda não tem valor
email_pessoal = None  # Usuário não forneceu email pessoal

# Verificando None
if email_pessoal is None:
    print("Email não cadastrado")

# ATENÇÃO: Use 'is' para None, não '=='
if resultado is None:  # ✅ Correto
    pass

if resultado == None:  # ⚠️ Funciona, mas não é pythônico
    pass
