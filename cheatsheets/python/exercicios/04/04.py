def gerenciar_agenda(agenda, operacao):
    """Gerencia operações em uma agenda de contatos"""
    if operacao == 'listar':
        return sorted(agenda.keys())

    elif operacao == 'emails':
        return [contato['email'] for contato in agenda.values()]

    return None

# Testes
agenda = {
    'João': {'email': 'joao@email.com', 'telefones': ['1111-1111', '2222-2222']},
    'Maria': {'email': 'maria@email.com', 'telefones': ['3333-3333']},
    'Pedro': {'email': 'pedro@email.com', 'telefones': ['4444-4444', '5555-5555', '6666-6666']}
}

print(gerenciar_agenda(agenda, 'listar'))
print(gerenciar_agenda(agenda, 'emails'))
