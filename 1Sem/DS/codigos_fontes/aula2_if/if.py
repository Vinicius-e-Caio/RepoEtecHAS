import os
os.system("cls")
"""
# utilizando o if composto (com else)
idade = int(input("Idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# utilizando o if simples (sem o else)
numero = float(input("Numero: "))

if numero < 0:
    numero = numero * -1

print(f"Numero: {numero}")

# utilizando o se encadeado
numero = int(input("Numero: "))

if numero < 0:
    print("Negativo")
else:
    if numero > 0:
        print("Positivo")
    else:
        print("Nulo")

# utilizando o elif
numero = int(input("Numero: "))

if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Nulo")
"""
# Comando de seleção (switch)

print("""
1 - Enunciado do exercicio 1
2 - Enunciado do exercicio 2
3 - Enunciado do exercicio 3
4 - Enunciado do exercicio 4
      """)
opcao = int(input("Escolha: "))

match opcao:
    case 1:
        print("executando o exercicio 1")
    case 2:
        print("executando o exercicio 2")
    case 3:
        print("executando o exercicio 3")
    case 4:
        print("executando o exercicio 4")
    case _:
        print("erro")


