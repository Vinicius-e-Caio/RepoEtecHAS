import os
os.system("cls")
key = 1
print("1 - Troca de Caractere")
print("2 - Separar Elementos por tipo")
print("3 - Inserir 10 itens num array")
opcao = int(input("Digite o número do exercício a ser escolhido: "))
while key != 0:
       match opcao:
              case 1:
                     os.system("cls")
                     def switcher(f:str, sea:str, swi:str)-> str:
                            result = f.replace(sea, swi)
                            return result
                     frase = input("Frase: ")
                     toSearch = input("Caractere a ser localizado: ")
                     toSwitch = input("Trocar pelo caractere: ")
                     print(switcher(frase, toSearch, toSwitch))
                     break
              case 2:
                     list = [45, 5.7, "Férias", True, False, 99, 34]
                     os.system("cls")
                     def to_separate(lista: list) -> None:
                            listint = []
                            listfloat = []
                            liststr = []
                            listbool = []
                            for c in range(len((list))):
                                   tipo = type(list[c])
                                   if tipo == int:
                                          listint.append(list[c])
                                   elif tipo == str:
                                          liststr.append(list[c])
                                   elif tipo == float:
                                          listfloat.append(list[c])
                                   elif tipo == bool:
                                          listbool.append(list[c])
                            print(listint, "\n",
                            listfloat, "\n",
                            liststr, "\n",
                            listbool, "\n")
                     to_separate(list)
                     break
              case 3:
                     os.system("cls")
                     list = []
                     i = 10
                     print("Digite . para sair")
                     while i > 0:
                            item = input("Digite: ")
                            if item == ".":
                                   break
                            list.append(item)
                            i = i - 1

                     if i == 0:
                            print("limite de 10 items excedido.")
                     else:
                            print("finalizado.")
                     print(list)
                     break
              case 0:
                     print("Finalizado.")
                     key = 0
                     break
              case _:
                     print("Digite uma opcao válida.")