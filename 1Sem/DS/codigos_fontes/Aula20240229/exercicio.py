import os
os.system("cls")
n = int(input("Digite o numero de lados: "))
med = int(input("Digite o tamanho"))
if n == 3:
    h = (med * n ** (1/2))/2
    print(h)
    area = (h * med )/2
    print("area =", area )
