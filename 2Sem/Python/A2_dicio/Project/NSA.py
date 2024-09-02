from os import system
from time import sleep
system("cls")

# Functions - For tests
def VerifyThis(NewData):
    if isinstance(NewData, str):
        return NewData
    if isinstance(NewData, int):
        return NewData
    
    return "invalid"
    

# Dicts / Variables
test = {}

print("Bem vindo ao mini NSA")
print( """
    0 - Sair
    1 - Adicionar novo Aluno | Nota (limite 10 alunos)
    2 - Editar Aluno | Nota
    3 - Listar os Alunos
    4 - Excluir um Aluno
    5 - Calcular a média da turma
    6 - Consultar um aluno
    7 - Apagar todos os alunos da sala
""")
key = 1
while key != 0:
    option = int(input("Digite sua Opção: "))
    match option:
        case 0:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("0 - Sair")
            print("\n")
            sleep(1)
            key = 0
            system("pause")
            system("cls")
    
        case 1:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("1 - Adicionar novo Aluno | Nota")
            print("Lembre-se o limite é de 10 alunos")
            print("\n")
            sleep(1)
            system("pause")
            system("cls")
            
        case 2:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

        case 3:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

        case 4:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

        case 5:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

        case 6:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

        case 7:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

        case _:
            print("DIgite uma opção válida")
