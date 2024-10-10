import os
os.system("cls")
with open("arquivos.txt", "w+", encoding="utf-8") as arq:
     arq.write("Linha 1\n")
     arq.write("                  Linha 2\n")
     arq.write("Linha 3\n")
     arq.write("Linha 4\n")
     # arq.seek(9) Seek é o cursor, é como se toda a atenção do código estivesse a partir desse cara
     # print(arq.readline()) readline é o comando que lê a linha que está o cursor
    
     arq.seek(0)
     lista = arq.readlines()
     print(lista)
     for linha in lista:
          print(linha.strip()) # strip é o comando que tira os espaços da string antes e depois dela, mas não dentro dela



# with open("arquivos.txt", "w+", encoding="utf-8") as arq:
#      arq.write("Linha1 \n")
#      arq.seek(0)
     