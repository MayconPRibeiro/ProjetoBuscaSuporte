from flask_login import LoginManager, UserMixin
from conexao_db import conectar

class User(UserMixin):
    def __init__(self, id, email, tipo):
        self.id = id
        self.email = email
        self.tipo = tipo

def load_user(user_id):
    conn = conectar()
    cursor = conn.cursor(dictionary = True)
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user['id'], user['email'], user['tipo'])
    return None
