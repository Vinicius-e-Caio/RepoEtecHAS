"""
crie um programa que permita o usuario
manipular um arquivo e os modos de abertura apresentados (exceto o +)
"""
while True:
    print("""
    Modo de abertura:
    ----------------
    'w' | write - gravar
    'r' | read - ler
    'a' | append - Edição de arquivo
    'x' | gravação em arquivo exclusivo
    '+' | gravar e ler ao mesmo tempo
    """)
    option = input("\nDigite sua opção:")
    name_arq = ""
    match option.lower():
        case "w":
            try:
                name_arq = input("Qual será o nome do arquivo: ")
                inserir = input("O que você deseja gravar nesse arquivo?: ")
                arq = open(name_arq + ".txt", "w", encoding = "utf-8")
                arq.write(inserir)
                arq.close()
            except:
                print("Erro ao gravar no arquivo")
        case "r":
            arq_open = input("Digite o mome do arquivo a ser aberto: ")
            try:
                arq = open(arq_open + ".txt", "r", encoding="utf-8")
                print(arq.read())
                arq.close()
            except FileNotFoundError:
                print(f"Arquivo Inexistente")
        case "a":
            arq_open = input("Digite o nome do arquivo que você quer adicionar algo: ")
            arq_eedit = input("Digite o que você quer adicionar no arquivo")
            try:
                arq = open(arq_open, "a", encoding="utf-8")
                arq.write(arq_eedit)
                arq.close()
            except FileNotFoundError:
                print(f"Arquivo Inexistente")
        case "x":
            try:
                arq = open(name_arq, "a", encoding="utf-8")
                print(arq.read())
                arq.close()
            except FileNotFoundError:
                print(f"Arquivo Inexistente")
