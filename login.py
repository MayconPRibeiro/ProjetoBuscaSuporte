from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import conexao_db
from flask import Flask, render_template, redirect, url_for, request, flash
from main import app
from conexao_db import conectar

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"

class User(UserMixin):
    def __init__(self, id, email, role):
        self.id = id
        self.email = email
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    conn = conectar()
    cursor = conn.cursor(dictionary = True)
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user['id'], user['email'], user['role'])
    return None
