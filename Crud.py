from conexao_db import conectar, conexao_db
import mysql.connector
from datetime import datetime
from zoneinfo import ZoneInfo
from fuzzywuzzy import process



def consultar():
    try:
        db_connection = conexao_db.conectar()
        con = db_connection.cursor(dictionary=True)
        sql = 'selct * from usuarios'
        con.execute(sql)
        resultado = con.fetchall()
        con.close()
        db_connection.close()

        if len(resultado) > 0:
            return resultado

        else:
            return 'Não Encontrei'

    except Exception as erro:
        return('Ops...' + str(erro))

def data_hora():
    fuso_horario = ZoneInfo('America/Sao_Paulo')
    data_hora = datetime.now(fuso_horario)
    return data_hora

from fuzzywuzzy import process
from conexao_db import conectar

def get_titles_from_db(user_type):
    conn = conectar()  # Conectar ao banco de dados
    cursor = conn.cursor()

    if user_type == 'cliente':
        cursor.execute("SELECT titulo FROM chamados WHERE permissoes = 'todos'")

    elif user_type == 'tecnico' or user_type == 'gestor':
        cursor.execute("SELECT titulo FROM chamados WHERE permissoes IN ('todos', 'tecnico')")

    titulos = [row[0] for row in cursor.fetchall()]
    conn.close()
    return titulos

def fuzzy_search(search_term, titles, limit=5):
    matches = process.extract(search_term, titles, limit=limit)
    return matches
