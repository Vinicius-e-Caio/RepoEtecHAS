contato = {
    'nome': 'eu',
    'idade': 50
}

print(contato)

contato['email'] = "@gmail.com"
print(contato)
contato['nome'] = "@gmail.com"
print(contato)
contato['Nome'] = "eu"
print(contato)

del contato['Nome']
print(contato)
contato.pop("Nome")