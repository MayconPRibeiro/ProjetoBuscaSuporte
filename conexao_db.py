import mysql.connector
import os
from flask import current_app
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        db_config = {
            'host' : os.getenv('DB_HOST'),
            'user' : os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }

        connection = mysql.connector.connect(**db_config)

        print("Conexão bem-sucedida!")
        return connection

    except mysql.connector.Error as err:
        return f"Erro de conexão: {err}"

    except Exception as e:
        return f"Erro inesperado ao tentar conectar: {e}"