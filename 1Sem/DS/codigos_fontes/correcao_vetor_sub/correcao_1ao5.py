# import subalgoritmos
from subalgoritmos import * # o * quer dizer TODOS
# ---------------------- PROGRAMA PRINCIPAL
# inicialicação do vetor
v = [45, -89, 32, 12, -12, 33]
import os
while True:
    os.system("cls")
    print(""" 
    0. S A I R
    1. Primeiro elemento do vetor. 
    2. Exiba somente os números negativos contidos no vetor.
    3. Soma dos elementos do vetor
    4. Média dos elementos do vetos
    5. Numeros ímpares contidos no vetor
    """)
    opcao = input("Escolha: ")
    if not opcao.isnumeric():
        input("Opção inválida!\nPressione alguma tecla para continuar . . .")
        continue
    opcao = int(opcao)
    match opcao:
        case 0:
            break
        case 1:
            print(f"Primeiro elemento: {primeiro_elemento(v)}")
        case 2:
            exibe_negativos(v)
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
    input("Digite algo para continuar . . .")
            