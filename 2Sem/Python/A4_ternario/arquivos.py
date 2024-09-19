import os
# ----------------- ARQUIVOS TEXTO
"""
Modo de abertura:
----------------
'w' | write - gravar
'r' | read - ler
'a' | append - Edição de arquivo
'x' | gravação em arquivo exclusivo
'+' | gravar e ler ao mesmo tempo

função open() -> abre um arquivo
--------------------------------
Sintaxe:
    <obj> = open("Nome_arquivo", "Modo_abertura")
"""

os.system("cls" if os.name == "nt" else "clear")

# arq = open("arq1.txt", "w", encoding="utf-8")
# arq.write("Será que vai dar namoro?")
# arq.write(f" katiau\n")
# arq.close()

# arq = open("arq1.txt", "a", encoding="utf-8")
# arq.write("\nNova linha")
# arq.close()

# Lendo um arquivo
try:
    arq = open("arq1.txt", "r", encoding = "utf-8")
    print(arq.read()) # Read carrega o arquivo inteiro
    arq.close()
except FileNotFoundError:
    print("Arquivo Inexistente.")

# arq = open("arq1.txt", "a+", encoding="utf-8")
# arq.write("outra coisa")
# print(arq.read())

arq = open("arq1.txt", "w+", encoding = "utf-8")
arq.write("Testando")
arq.seek(4)
print(arq.read())
arq.close()

# Operador de contexto with
caminho = "d:\\aula\\ds\\"
caminho += "arq1.txt"
with open(caminho, "w+", encoding = "utf-8") as arq:
    arq.write("Testando")
    arq.seek(4)
    print(arq.read())