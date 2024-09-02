# laço enquanto: while

# x = 1
# while x <= 10:
#     print(x)
#     x = x + 1
# print("Edson")
"""
x = 1
while x <= 10:
    print(x)
    x = x + 1
    if x == 5:
        break # intrrrompe a execução do laco
else:
    print("Será executado se não houver interrupção")
"""

opcao = ""
while opcao != "Edson":
    opcao = input("Digite Edson:")
    if opcao != "Edson":
        continue
else:
    print("Voce digitou edson")
