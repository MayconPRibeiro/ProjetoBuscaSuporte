'''from Crud import consultar

dados = consultar()

print(dados)'''
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
connection = None  # Define a variável connection antes do bloco try

try:
    db_config = {
        'host' : os.getenv('DB_HOST'),
        'user' : os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }

    connection = mysql.connector.connect(**db_config)
    print("Conexão bem-sucedida")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if connection and connection.is_connected():  # Verifica se a conexão foi criada e está conectada
        connection.close()
        print("Conexão fechada")
