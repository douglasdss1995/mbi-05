def validar_senha(senha):
    """Valida se uma senha atende aos critérios de segurança"""
    if len(senha) < 8:
        return (False, "Menos de 8 caracteres")

    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    if not tem_maiuscula:
        return (False, "Falta letra maiúscula")
    if not tem_minuscula:
        return (False, "Falta letra minúscula")
    if not tem_numero:
        return (False, "Falta número")

    return (True, "Senha válida")

# Testes
print(validar_senha("Senha123"))
print(validar_senha("senha123"))
print(validar_senha("SENHA123"))
print(validar_senha("SenhaForte"))
print(validar_senha("Sen1"))
print(validar_senha("MinhaSenh@123"))
