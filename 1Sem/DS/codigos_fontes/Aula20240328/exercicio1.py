# dadas 3 notas, tirar a menor e calcular a média das outras duas
def menor3n(n1: float, n2: float, n3: float) -> float:
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

def media2maiores(n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3 - menor3n(n1, n2, n3)) / 2

# ------------- PROGRAMA PRINCIPAL
import os
os.system("cls")
nota1 = 5
nota2 = 1
nota3 = 2
print(f"Media: {media2maiores(nota1, nota2, nota3)}")

# 1. faça uma função que calcule delta
# 2. faça uma função que calcule x1
# 3. faça uma função que calcule x2



