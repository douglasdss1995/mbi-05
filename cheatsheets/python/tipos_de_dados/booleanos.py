# Valores booleanos
ativo = True
desativado = False

# Comparações retornam booleanos
10 > 5          # True
10 < 5          # False
10 >= 10        # True
10 == 10        # True (igualdade)
10 != 5         # True (diferente)

# Operadores lógicos
True and False  # False
True or False   # True
not True        # False

# Valores considerados False (Falsy)
bool(0)         # False
bool("")        # False (string vazia)
bool([])        # False (lista vazia)
bool({})        # False (dicionário vazio)
bool(None)      # False

# Valores considerados True (Truthy)
bool(1)         # True
bool("texto")   # True
bool([1, 2])    # True
bool({"a": 1})  # True

# Uso prático no Django
usuario_autenticado = True
if usuario_autenticado:
    print("Acesso permitido")
