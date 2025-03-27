import conexao_db
import mysql.connector
from datetime import datetime
from zoneinfo import ZoneInfo


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

