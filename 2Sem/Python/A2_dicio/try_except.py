"""
try:
    comandos
except: 
    codigos caso dê ruim
else:
    codigos caso não haja erro
finally:
    codigos para circunstâncias 
"""



from os import system
system('cls')

try:
    valor1 = float(input('Valor 1: '))
    valor2 = float(input('Valor 2: '))
    divisao = valor1 / valor2
    print(divisao)
except ValueError:
    print("Digite um valor númerico")
except ZeroDivisionError as err:
    print(f"Divisão 2? onde já se viu dividir número com 0 {err}")
except:
    print("CHAMA O DEVKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
else:
    print("divisao efetuada com sucess")
finally:
    print("saindo do sys")