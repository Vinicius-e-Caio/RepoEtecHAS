import os
os.system("cls")
# ------------------ SUBALGORITMOS
def exibe_vetor(vet: list) -> None:
    for i in range(0, 5, 1):
        print(f"Posição {i}: {vet[i]}")

# 1. Fazer uma Função que retorne o primeiro elemento do 
# vetor. 
def exibe_primeiro_elemento(vet: list) -> int:
    return vet[0]
 

# ------------------ PROGRAMA PRINCIPAL
#     0   1   2   3   4
# iniciando o vetor
v = [45, 34, 23, 12, 67]
exibe_vetor(v)
print(exibe_primeiro_elemento(v))

# Dado o vetor por parâmetro e a posição a ser exibida, faça
# uma função chamada 'exibe_posicao' que exiba o elemento 
# correspondente. 
# Considerar que o vetor tenha 5 elementos, caso a posição
# informada seja fora deste intervalo, exibir a primeira 
# posição

