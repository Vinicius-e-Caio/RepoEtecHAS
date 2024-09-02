import os
os.system("cls")

# --------------- DEFINIÇÃO DOS SUBALGORITMOS
# função que soma dois numeros
def soma2n(n1: float, n2: float) -> float:
    return n1 + n2

# função que calcula a média de dois numeros
def media2n(n1: float, n2: float) -> float:
    return soma2n(n1,n2)/2

# procedimento que efetua uma saudação
def saudacao() -> None:
    print("Bom dia, usuário")

# procedimento que efetua uma saudação
def saudacao1(usuario: str) -> None:
    print(f"Bom dia, {usuario}")

# procedimento que efetua uma saudação
def saudacao2(usuario: str, hora: int) -> None:
    if hora < 12:
        print(f"Bom dia, {usuario}")
    elif hora < 18:
        print(f"Boa tarde, {usuario}")
    else:
        print(f"Boa noite, {usuario}")

# Preencher o vetor
def preenche_vetor() -> None:
    for i in range(5):
        input(f"Posicao {i} = ")

    
# Exibir o vetor
def exibe_vetor() -> None:
    for i in range(5):
        print(f"Posicao {i} = {v[i]}")

#1. Fazer uma Função que retorne o primeiro elemento do vetor. 
#	x = primeiro_elemento(v)
# 	>> x valerá 45
def primeiro_elemento() -> int:
    return v[0]




# --------------- PROGRAMA PRINCIPAL
print(f"Soma = {soma2n(45,98)}")
print(f"Média = {media2n(45,98)}")
saudacao()
saudacao1("Edson")
saudacao2("Edson",21)
v = [3,5,87,6,5]
#preenche_vetor()
exibe_vetor()
print(primeiro_elemento())
