from os import system
from time import sleep
system("cls")

# Functions - For tests
def VerifyThis(newData, type):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special = ',. '
    if newData == '':
        return None
    if type == str:
        for i in range(len(newData)):
            if newData[i].lower() not in letters and newData[i] not in special:
                newData = None
                break
        for x in notas.keys():
            if x.lower() == newAluno.lower():
                print(f"Já existe um aluno com esse nome.\n")
                system("pause")
                return None
        return newData
    if type == int:
        newData = newData.replace(' ', '')
        for i in range(len(newData)):
            if newData[i] not in numbers:
                if newData[i] not in special:
                    return None
                if newData[i] == ',':
                    system("cls")
                    print(f"Favor use . ao invés de ,")
    
                    print(f"{newData} foi alterado para {newData.replace(',', '.')} \n")
                    system("pause")
                    newData = newData.replace(',', '.')
        return float(newData)
    return None

def editarAluno(nomeAluno:  str, newNota: str) -> None:
    newNota = newNota.replace(",", ".")
    newNota = float(newNota)
    if newNota < 0 or newNota > 10:
        print("Nota inválida.\n")
        return None
    found = None
    for keys in notas.keys():
        if keys.lower() == nomeAluno.lower():
            found = True
    if not found:
        print(f"Aluno {nomeAluno.lower()} não encontrado!\n")
        system("pause")
        system("cls")
        return 
    try:
        notas[nomeAluno] = newNota
        print(f"Nota do aluno {nomeAluno.lower()} alterada com sucesso!\n")
        system("pause")
        system("cls")   
    except:
        print(f"Ocorreu um erro.")

def listAluno() -> None: 
    if not notas.keys():
        print("Nenhum aluno cadastrado!")
        return None
    print("Alunos cadastrados:")
    for aluno, nota in notas.items():
        print(f"{aluno}: {nota}")

def ExcluirAl(nomeAl: str) -> None:
    while True:
        if nomeAl in notas:
            try:
                del notas[nomeAl]
                print(f"Aluno {nomeAl} excluído com sucesso!")
                break
            except:
                print("Ocorreu um erro ao tentar excluir o aluno.")
                
        else:
            print(f"Aluno {nomeAl} não encontrado!")
            confirmRetry = input("Quer tentar de novo? (S/N)")
            match confirmRetry.upper():
                case 'S':
                    nomeAl = str(input("Digite novamente: "))
                case 'N':
                    break
                case _:
                    print("Digite um valor válido.")
                    continue

# Dicts / Variables
retry = ""
notas = {}

key = 1
while key != 0:
    print("Bem vindo ao mini NSA")
    print( """
        1 - Adicionar novo Aluno | Nota (limite 10 alunos)
        2 - Editar Aluno | Nota
        3 - Listar os Alunos
        4 - Excluir um Aluno
        5 - Calcular a média da turma
        6 - Consultar um aluno
        7 - Apagar todos os alunos da sala
        0 - Sair
    """)
    try:
        option = input("Digite sua Opção: ")
        if not option.isdigit():
            print(f"Opção inválida!\n")
            system("pause")
            system("cls")
            continue
        else:
            option = int(option)
    except ValueError:
        print(f"Digite um número.\n")
    except NameError as error:
        print(f"Digite um número.\n", error)

    match option:
        case 1:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("1 - Adicionar novo Aluno | Nota")
            print("Lembre-se o limite é de 10 alunos")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            while True:
                contador = 0
                for keys in notas.keys():
                    contador = contador + 1
                if contador == 10:
                    print("Limite de alunos atingido!")
                    system("pause")
                    break
                system("cls")
                newAluno = VerifyThis(input("Aluno: "), str)
                
                if newAluno == None:
                    print(f"Inválido \n")
                    system("pause")
                    continue
                newNota = VerifyThis(input("Nota: "), int)
                if newNota == None:
                    print(f"Inválido \n")
                    system("pause")
                    continue
                if newNota < 0 or newNota > 10:
                    print(f"Nota inválida.\n")
                    system("pause")
                    continue
                while True: 
                    system("cls")
                    print(f"Aluno: {newAluno} \nNota: {newNota}")
                    confirm = input("Confirma? (S/N): ")
                    match confirm.upper():
                        case 'S':
                            notas[newAluno] = newNota
                            print(f'Adicionado! \n')
                            system("pause")
                            system("cls")
                            break
                        case 'N':
                            break
                        case _:
                            print("Digite um valor válido.")
                            continue
                    break
                if len(notas) < 10:
                    while True:
                        retry = input("Adicionar outro? (S/N): ")
                        match retry.upper():
                            case 'S':
                                break
                            case 'N':
                                retry = None
                                break
                            case _:
                                print("Digite um valor válido.")
                                continue
                        break
                    if not retry == None:
                        continue
                    break
                else:
                    print("Limite de 10 Aluno excedido.")
                    break
        
        case 2:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("2 - Editar Aluno | Nota")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            if len(notas) > 0:
                while True:
                    aluno = str(input("Digite o nome do aluno para alterar sua nota: "))
                    if VerifyThis(aluno, str) == None:
                        print("Nome inválido!!")
                        continue
                    nota = input("Digite a nova nota: ")
                    if VerifyThis(nota, int) == None:
                        print("Nota inválida!!")
                        continue
                    editarAluno(aluno, nota)
                    while True:
                        retry = input("Adicionar outro? (S/N): ")
                        match retry.upper():
                            case 'S':
                                break
                            case 'N':
                                retry = None
                                break  
                            case _:
                                print(f"Digite um valor válido.\n")
                                system("pause")
                                system("cls")
                                continue
                    if not retry == None:
                        continue
                    break
            else:
                print(f"Você não possui alunos cadastrados. \n")
                system("pause")
                system("cls")

        case 3:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("3 - Listar os Alunos")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            listAluno()
            print(f"\n")
            system("pause")
            system("cls")

        case 4:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("4 - Excluir um Aluno")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            if len(notas) > 0:
                while True:
                    nameAl = input("Digite o nome do Aluno: ")
                    
                    if VerifyThis(nameAl, str) == None:
                        print("Nome inválido!!")
                        continue
                    break
                ExcluirAl(nameAl)
            else:
                print(f"Você não possui alunos cadastrados. \n")
                system("pause")
                system("cls")
          
        case 5:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("5 - Calcular a média da turma")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            soma = 0
            if len(notas) > 0:
                for x in notas.values():
                    soma = x + soma
                media = soma / len(notas)
                print("a média da turma é: ", media)
                system("pause")
                system("cls")
            else:
                print(f"Você não possui alunos cadastrados. \n")
                system("pause")
                system("cls")

        case 6:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("6 - Consultar um aluno")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            if len(notas) > 0:
                while True:
                    search = VerifyThis(input("Procurar Aluno: "), str)
                    
                    if search == None:
                        print("Digite um nome válido")
                        system("pause")
                        system("cls")
                        continue
                    if search in notas.keys():
                        print(f"\n")
                        print(f"Nome..........: ", search)
                        print(f"Nota..........: ", notas[search])
                        print(f"\n")
                        while True:
                            option = input("Tentar Novamente? (S/N): ")
                            print(f"\n")
                            match option.upper():
                                case 'S':
                                    option = True
                                case 'N':
                                    break
                                case _:
                                    print("Digite uma opção válida (S/N)")
                                    print(f"\n")
                                    continue
                            break
                        if option == True:
                            continue
                        break
                    else:
                        print(f"\n")
                        print(f"{search} não foi encontrado.")
                        print(f"\n")
                        system("pause")
                        system("cls")
            else:
                print(f"Você não possui alunos cadastrados. \n")
                system("pause")
                system("cls")
        
        case 7:
            # Prints
            system("cls")
            print("Você escolheu:") 
            print("7 - Apagar todos os alunos da sala")
            print(f"\n")
            system("pause")
            print(f"\n")
            # Main
            if len(notas) > 0:
                while True:
                    option = input("Você tem certeza? (S/N): ")
                    match option.upper():
                        case 'S':
                            option = True
                            break
                        case 'N':
                            break
                        case _:
                            print("Digite uma opção válida (S/N)")
                            continue
                if option == True:
                    notas.clear()
                    print("Todos os alunos foram deletados.")
                    system("pause")
                    system("cls")
            else:
                print(f"Você não possui alunos cadastrados. \n")
                system("pause")
                system("cls")
                
        case 0:
            key = 0

        case _:
            print("Digite uma opção válida")
            system("pause")
            system("cls")
