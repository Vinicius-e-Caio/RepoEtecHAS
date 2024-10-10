import os
os.system("cls")

"""
1 - Inserir comentarios
2 - Contar quantas vogais
3 - Contar quantas palavras
0 - Sair


Definições:
1. Cada comentário será inserido pelo usuário e será gravado em 1 linha no arquivo
2. Contar as vogais de todos os comentário
3. Contar a quantidade de palavras de todos os comentários
"""
print("""
1 - Inserir comentarios
2 - Contar quantas vogais
3 - Contar quantas palavras
0 - Sair
      """)
contadorVogais = 0
contadorPalavras = 0
while True:
    try:
        option = int(input("Qual a opção desejada:"))
    except ValueError as error:
        print("Você deve digitar algo valido...")
        continue
    match option:
        case 1:
            print("1 - Inserir comentarios\n")
            with open("arquivos.txt", "a", encoding="utf-8") as arq:
                comentario = input("Dgite o comentário que deseja adicionar: ")
                arq.write(comentario + "\n")
        case 2:
            try:
                print("2 - Contar quantas vogais \n")
                with open("arquivos.txt", "r", encoding="utf-8") as arq:
                    arq.seek(0)
                    lista = arq.readlines()
                    content = "".join(lista)
                    vogais = "aeiou"
                    for vogal in content:
                        if vogal.lower() in vogais:
                            contadorVogais += 1
                    print("Os comentários ao todo tem:",contadorVogais , "vogais")
            except FileNotFoundError as error:
                print("Execute a função 1 primeiro para utilizar as outras")
                continue
        case 3:
            try:
                print("3 - Contar quantas palavras\n")
                with open("arquivos.txt", "r", encoding="utf-8") as arq:
                    arq.seek(0)
                    lista = arq.readlines()
                    content = "".join(lista)
                    content = content.split()
                    for palavras in content:
                        contadorPalavras += 1
                    print("Os comentários ao todo tem:",contadorPalavras , "palavras")
            except FileNotFoundError as error:
                print("Execute a função 1 primeiro para utilizar as outras")
                continue
        case 0:
            break
        case _:
            print("Digite uma opção válida")
