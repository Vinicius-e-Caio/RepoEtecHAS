# --------------- SUBALGORITMOS
# faça uma função que calcule a soma de 2 numeros
def soma2n(n1: float, n2: float) -> float:
    return n1 + n2

# faça uma função que calcule a média de 2 numeros
def media2n(n1: float, n2: float) -> float:
    return soma2n(n1, n2) / 2
# Exibir uma saudacao
def saudacao() -> None:
    print("Salve galera, boa tarde!")
# Exibir uma saudacao com parametro
def saudacao2(pessoa: str) -> None:
    print(f"Salve {pessoa}, boa tarde!")
# Exibir uma saudacao com parametros
def saudacao3(pessoa: str, hora: int) -> None:
    if hora < 12:
        print(f"Salve {pessoa}, bom dia!")
    elif hora < 18:
        print(f"Salve {pessoa}, boa tarde!")
    else:
        print(f"Salve {pessoa}, boa noite!")
# --------------- PROGRAMA PRINCIPAL
import os
os.system("cls")
valor1 = 56
valor2 = 45
resposta = soma2n(valor1, valor2)
print(f"Resposta = {resposta}")
resposta = media2n(valor1, valor2)
print(f"Resposta = {resposta}")
saudacao()
saudacao2("Maria")
saudacao3("Paulo", 22)


