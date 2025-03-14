import conexao_db
import mysql.connector

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

