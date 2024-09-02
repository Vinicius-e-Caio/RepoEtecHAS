import os
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