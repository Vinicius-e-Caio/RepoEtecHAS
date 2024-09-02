import os

while True:
    os.system("cls")
    print("""
    0 - Sair
    1 - Tabuada
    2 - Vogal
           """)
    opcao = input("Escolha: ")
    match opcao:
        case "0":
            break
        case "1":
            tab = int(input("Tabuada: "))
            for i in range(1,11,1):
                print(f"{tab} x {i} = {tab*i}")
        case "2":
            cont = 0
            for i in range(0,5,1):
                c = input("Caractere:")
                if c=='a' or c=='e' or c=='i' or c=='o' or c == 'u' or c=='A' or c=='E' or c=='I' or c=='O' or c == 'U':
                    cont = cont + 1    
            print(f"Vogais: {cont}")
        case _:
            print("Opcao invalida!")
    input("Digite algo para continuar...")