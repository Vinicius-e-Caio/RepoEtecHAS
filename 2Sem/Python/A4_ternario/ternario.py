"""
[<variavel> = ] <comando True> if <condicao> else <comando False>
"""
# Sem utilizar a variavel
import os
os.system("cls" if os.name == "nt" else "clear")
os.system("dir" if os.name == "nt" else "ls")
idade = 1
print("Maior de idade") if idade >= 18 else print("Menor de idade")

# Utilizndo variavel

os.system("cls" if os.name == "nt" else "clear")
"""
[<variavel> = ] <comando True> if <condicao> else <comando False>
"""
venda = 5000
bonus = 50 if venda > 3000 else 30
print(venda, bonus)

# Fazendo parte do calculo
os.system("cls" if os.name == "nt" else "clear")
venda = 5000
venda_atualizada = venda - (venda * 0.1 if venda > 1000 else venda * 0.05)
print(venda, venda_atualizada)