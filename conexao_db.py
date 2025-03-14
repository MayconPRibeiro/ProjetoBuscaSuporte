import mysql.connector

db_config = {
    'host' : '',
    'user' : 'root',
    'password' : 'Assecont1973',
    'database' : 'DB_Busca'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection