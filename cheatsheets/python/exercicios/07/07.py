def classificar_nota(nota):
    """Classifica uma nota numérica em conceito"""
    if nota < 0 or nota > 100:
        return "Inválido"
    elif nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

# Testes
print(classificar_nota(95))
print(classificar_nota(82))
print(classificar_nota(59))
print(classificar_nota(105))
print(classificar_nota(-5))
print(classificar_nota(70))
print(classificar_nota(100))
