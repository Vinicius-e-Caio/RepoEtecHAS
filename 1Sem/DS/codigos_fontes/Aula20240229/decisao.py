import os
os.system("cls")

# Estrutura de decisão if
# if - simples (sem o else)
"""
n = int(input("Digite um numero: "))
if n < 0:
    n = -n
print("Numero: ", n)
"""
# if - composto (com o else)
"""
n = int(input("Digite um numero: "))
if n < 0:
    print(f"O numero {n} é negativo")
else:
    print(f"O numero {n} NÃO é negativo")
"""   
"""
# if - encadeado
n = int(input("Digite um numero: "))
if n < 0:
    print("Negativo")
else:
    if n > 0:
        print("Positivo")
    else:
        print("Nulo")
""" 
"""
# if - elif
n = int(input("Digite um numero: "))
if n < 0:
    print("Negativo")
elif n > 0:
    print("Positivo")
else:
    print("Nulo")
"""        
# match case
print("""
1 - Exercicio 1
2 - Exercicio 2
3 - Exercicio 3
4 - Exercicio 4
    """)
opcao = int(input("Escolha: "))
match opcao:
    case 1:
        print("Executando o exercicio 1")
    case 2:
        print("Executando o exercicio 2")
    case 3:
        print("Executando o exercicio 3")
    case 4:
        print("Executando o exercicio 4")
    case _:
        print("Opção inválida")