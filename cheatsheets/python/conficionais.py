# If simples
idade = 18
if idade >= 18:
    print("Maior de idade")

# If-else
idade = 16
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# If-elif-else
nota = 75
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")

# Condições múltiplas
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

if idade < 18 or not tem_carteira:
    print("Não pode dirigir")

# Operador in
frutas = ["maçã", "banana", "laranja"]
if "banana" in frutas:
    print("Tem banana!")

# Verificando None
email = None
if email is None:
    print("Email não informado")

# Operador ternário (condicional em uma linha)
idade = 20
status = "Maior" if idade >= 18 else "Menor"


# Match-case (Python 3.10+)
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Não encontrado")
    case 500:
        print("Erro do servidor")
    case _:  # default
        print("Outro status")


# Exemplo Django com match-case
def processar_requisicao(metodo):
    match metodo:
        case "GET":
            return "listar dados"
        case "POST":
            return "Criar dados"
        case "PUT" | "PATCH":  # Múltiplas opções
            return "Atualizar dados"
        case "DELETE":
            return "Deletar dados"
        case _:
            return "Erro método inválido"
