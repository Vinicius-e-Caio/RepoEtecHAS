# Exercício: permitir ao usuário digitar os dados nome, idade e email e gravá-lo no arquivo json.
import json
from os import system
system("cls")

# Globals
caminho = "D:\\Vinicius_e_Caio_2BI\\RepoEtecHAS\\2Sem\\Python\\A6_json\\Exercícios\\jsons\\"
count = 0
nameArq = str(input("Nome do Arquivo Json: ")) + ".json"
while True:
    system("cls")
    try:
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        email = str(input("Email: "))
    except ValueError as err:
        print("Tente usar outra coisa.")
        print(f"{err}")
        system("pause")
        system("cls")
        continue


    # Criando um dicionário
    dicio = {
        count:{
            'nome': nome,
            'idade': idade,
            'email': email
        }
    }


    system("pause")
    system("cls")                


    print("""
Adicionar outro?
    1 - Sim
    2 - Não 
    """)
    escolha = int(input(": "))
    if escolha == 1:
        count += 1
        continue
    
    with open(caminho + nameArq, "r") as arq:
        dados_lidos = json.load(arq)
        for k,v in dados_lidos.items():
            print(f"Registro...: {k}")
            for k1, v1 in v.items():
                print("\t" + k1 + ":" + str(v1))
        break

