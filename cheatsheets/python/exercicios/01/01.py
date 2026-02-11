def validar_email(email: str) -> bool:
    """Valida formato de email.

    Args:
        email (str): O email a ser validado.

    Returns:
        bool: True se o email for válido, False caso contrário.
    """
    # Verificar tamanho mínimo
    if len(email) < 5:
        return False

    # Verificar se tem exatamente um @
    if email.count("@") != 1:
        return False

    # Verificar se tem exatamente um ponto .
    if email.count(".") != 1:
        return False

    # Dividi o e-mail em nome e dominio
    partes = email.split("@")
    nome = partes[0]
    dominio = partes[1]

    # Verificar se domínio tem pelo menos um ponto
    if "." not in dominio:
        return False

    # Verificar se tem conteúdo antes e depois do @
    if len(nome) == 0 or len(dominio) == 0:
        return False

    return True


# Testes
print(validar_email("usuario@email.com"))  # True
print(validar_email("teste.usuario@empresa.com.br"))  # True
print(validar_email("usuario@email"))  # False
print(validar_email("@email.com"))  # False
print(validar_email("usuario.email.com"))  # False
print(validar_email("a@b.c"))  # True
