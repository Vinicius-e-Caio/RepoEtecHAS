tabela = []

contato = {
    'nome': 'Vini',
    'idade': 50
}



from os import system
system("cls")
tabela.append(contato.copy())

print(tabela)

# contato["nome"] = input("Nome: ")
# contato["idade"] = input("Idade: ")
contato["nome"] = "Maria"
contato["idade"] = 20
tabela.append(contato)
print(tabela)


#Exibe as keys()
for k in contato.keys():
    print(k)
#Exibe as value()
for v in contato.values():
    print(v)
#Exibe os dois
for k, v in contato.items():
    print(k, v)

for i in range(len(tabela)):
    print(f"nome: {tabela[i]['nome']}")
    print(f"Idade: {tabela[i]['idade']}\n")