# ###
# # Dicionário
# # Possui chaves e valores => Key e Value
# # Key => Chave
# # Value => Conteúdo associado à chaves
# # Keys => Todes es chaves
# # Values => São todes es valores
# # Item => Conjumto key, valor
# # Items => São todos os conjuntos do dicionário
# ###
# def exibicao_manual(d: dict) -> None:
#     os.system("cls");
#     print(f"Nome..........: ", d['nome'])
#     print(f"Idade..........: ", d['idade'])
#     print(f"Cazada?..........: ", d['casada'])
#     print(f"Altura..........: ", d['altura'])

# def exibicao_metodos(d: dict) -> None:
#     os.system("cls")
#     for chave, valor in d.items():
#         print(f"{chave} -> {valor}")


# import os
# os.system("cls")
# # Criando um dicionário
# dicionario = {} # ou dict
# print(dicionario)

# contato = {
#     #'key' : value
#     'nome': 'Eliane',
#     'idade': 45,
#     'casada': True
# }
# print(contato)

# print(f"Nome..........: ", contato['nome'])
# print(f"Idade..........: ", contato['idade'])
# print(f"Cazada?..........: ", contato['casada'])

# contato['altura'] = 1.63

# print(f"Altura..........: ", contato['altura'])

# os.system("cls")
# # print(contato.keys()) #objeto bruto
# # print(list(contato.keys()))
# # for chave in contato.keys():
# #     print(chave)

# # print(contato.values()) #objeto bruto
# # print(list(contato.values()))
# # for chave in contato.values():
# #     print(chave)

# # print(contato.items()) #objeto bruto
# # print(list(contato.items()))
# # for chave in contato.items():
# #     print(chave)

# #manipular os items
# print(contato.items())
# print(list(contato.items())) # Criando uma lista
# for chave, valor in contato.items():
#     print(f"{chave} -> {valor}")
# contato['altura'] = 1.63
# exibicao_metodos(contato);

notas = {
    'Edson': 10,
    'Marion': 10,
    'Luana': 3
}

print(notas)

del notas['Edson']
notas.pop('Edson')
# notas.clear()
print(notas)