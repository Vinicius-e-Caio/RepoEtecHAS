import pyodbc
import pandas as pd

def get_pets_data():
    print("GET ai po")
try:
    conn = pyodbc.connect('DRIVER={SQL Server};'
            'SERVER=amigo_secreto.mssql.somee.com;'
            'DATABASE=amigo_secreto;'
            'UID=Vini_dev_SQLLogin_1;'
            'PWD=kov33gmdsc;'
            'TrustServerCertificate=True;'
            'Persist Security Info=False;'
            'Packet Size=4096;')
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as error:
    print(error)
else:
    print("Conectado ao Banco de dados")