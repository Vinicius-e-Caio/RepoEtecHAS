import os

os.system("cls")

def switcher(f:str, sea:str, swi:str)-> str:
     result = f.replace(sea, swi)
     return result

frase = input("Frase: ")
toSearch = input("Caractere a ser localizado: ")
toSwitch = input("Trocar pelo caractere: ")

print(switcher(frase, toSearch, toSwitch))