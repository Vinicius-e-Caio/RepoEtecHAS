# Comentário de uma linha
"""
Comentario de mais 
de uma linha
"""
'''
Comentario de mais 
de uma linha
'''

#  print é o comando de saída de dados - printf()
print("Executando via vscode")

# Variáveis
x = 5
print(x, type(x)) # type mostra o tipo da variável
x = 9.8
print(x, type(x))
x = "Edson"
print(x, type(x))
x = False
print(x, type(x))
x = "5" + "6"
print(x)

# tipos de dados em Python
"""
int - inteiro
float - real
str - string (texto)
bool - booleano (lógico)
"""

# Casting - mudança de tipo da variável
x = "5"
y = "6"
z = float(x) + float(y)
print(z)
z = int(x) + int(y)
print(z)
rm = str(1254)
print(rm, type(rm))

# input - Entrada de dados (scanf)
"""
valor1 = input("Digite um valor: ")
valor1 = float(valor1)
valor2 = input("Digite outro valor: ")
valor2 = float(valor2)
resposta = valor1 + valor2
print(resposta)
"""
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
resposta = valor1 + valor2
print(resposta)

# Exercício: fazer um programa que leia os anos
# de vida do usuário e mostre a quantidade de
# dias de vida