'''from Crud import consultar

dados = consultar()

print(dados)'''

from Crud import data_hora
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
print(f"DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")

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


'''TESTE DE CRIAR SENHA HASH
from werkzeug.security import generate_password_hash

# Senha do usuário
password = "teste"

# Gerar o hash da senha
hashed_password = generate_password_hash(password)

print(f'Armazene: {hashed_password}')'''

''' TESTANDO HASH
from werkzeug.security import check_password_hash

# Hash armazenado no banco de dados
hashed_password = "scrypt:32768:8:1$e6dQbYmmdwk30tfH$bd07e27aaafde23f91bd2940f4e6b578f63362d41441d23cbc14d05653e6a39befe9e380edd370d19f1c4ed435c9b53f887f4ed253ab2331afa8441bdc925610"

# Senha fornecida pelo usuário
senha_fornecida = "teste"

# Verificar se a senha fornecida corresponde ao hash armazenado
if check_password_hash(hashed_password, senha_fornecida):
    print("A senha fornecida é válida!")
else:
    print("A senha fornecida é inválida!")'''