import json
from os import system
system("cls")

# Criando um dicionário
contato = {
    'nome':'Edson',
    'idade':50,
    'email':'eds@mail.com'
}

# Gravando o dicionário no arquivo
with open("arquivo2.json", "w") as arq:
    json.dump(contato, arq)

# Ler e imprimir o arquivo json
with open("arquivo2.json", "r") as arq:
    dados_lidos = json.load(arq)
    print(dados_lidos)

# Modificar o conteudo de um arquivo json
with open("arquivo2.json", "r") as arq:   
    dados_modificados = json.load(arq)
    # Modificando os dados
    dados_modificados["idade"] = 45
    dados_modificados["email"] = "emailjsoneds@mail.com"

# Gravando os arquivos modificados no arquivo json
with open("arquivo2.json", "w") as arq:
    json.dump(dados_modificados, arq)

# Lendo o arquivo modificado
with open("arquivo2.json", "r") as arq:
    dados_modificados_lidos = json.load(arq)
    print(dados_modificados_lidos)

for k, v in dados_modificados_lidos.items():
    print(f"{k} -> {v}")