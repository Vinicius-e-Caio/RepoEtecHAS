import json
from os import system
system("cls")
pessoas = {
    'pessoa1':{
        'nome':'Edson',
        'idade':50,
        'email':'eds@mail.com'
    },
    'pessoa2':{
        'nome':'Marion',
        'idade':70,
        'email':'mrn@mail.com'
    }
}
# exibindo o dicionário
print("\nDicionário\n")
print(pessoas)

pessoas_json = json.dumps(pessoas, indent=4)
print("\nJson:\n")
print(pessoas_json)

# Gravando no arquivo Json
with open("arquivo.json", "w") as file:
    file.write(pessoas_json)

# Lendo o arquivo Json
with open("arquivo.json", "r") as file:
    # Leu o arquivo e colocou no objeto json
    pessoas_json = file.read()
    # Converteu o objeto em um dicionario
    pessoas = json.loads(pessoas_json)

system("cls")
print(pessoas)
print(pessoas_json)

for k,v in pessoas.items():
    print(f"Registro...: {k}")
    for k1, v1 in v.items():
        print("\t" + k1 + ":" + str(v1))