'''from Crud import consultar

dados = consultar()

print(dados)'''


import mysql.connector

connection = None  # Define a variável connection antes do bloco try

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='FitAirlines'
    )
    print("Conexão bem-sucedida")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if connection and connection.is_connected():  # Verifica se a conexão foi criada e está conectada
        connection.close()
        print("Conexão fechada")
