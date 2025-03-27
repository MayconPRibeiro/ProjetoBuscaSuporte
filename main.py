from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from login import User, load_user
from flask_login import LoginManager
from conexao_db import conectar
from Crud import data_hora

import mysql.connector
import os
from flask import current_app
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__) #objeto flask
app.secret_key = 'ASDB157;;8963' #chave secreta

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"

@login_manager.user_loader
def load_user_by_id(user_id):
    return load_user(user_id)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if not email or not senha:
            flash('Todos os campos são obrigatórios','erro')
            return redirect (url_for('index'))

        conn = conectar()

        if isinstance(conn, str):
            flash(conn, 'erro')
            return render_template("index.html")

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if user and check_password_hash(user['senha'], senha):
            user_obj = User(id=user['id'], email=user['email'], tipo=user['tipo'], nome=user['nome'])
            login_user(user_obj)
            flash("Seja Bem Vindo(a)!", "sucesso")

            if current_user.tipo == 'gestor':
                return redirect(url_for('pagina_inicial_gestor'))
            elif current_user.tipo == 'tecnico':
                return redirect(url_for('pagina_inicial_tecnico'))
            elif current_user.tipo == 'cliente':
                return redirect(url_for('pagina_inicial_cliente'))
            
            else:
                flash('Ops, Algo deu errado', 'erro')
                return redirect(url_for('index'))

        else:
            flash('Login ou Senha inválidos', 'erro')

    return render_template("index.html")
    #return render_template("pagina_inicial_gestor.html")

@app.route("/pagina_inicial")
@login_required
def pagina_inicial():

    
    if current_user.tipo == "gestor":
        return render_template("pagina_inicial_gestor.html")
    elif current_user.tipo == "tecnico":
        return render_template("pagina_inicial_tecnico.html")
    elif current_user.tipo == "cliente":
        return render_template("pagina_inicial_cliente.html")
    else:
        return redirect(url_for("index"))


@app.route("/pagina_inicial_tecnico")
@login_required
def pagina_inicial_tecnico():
    if current_user.tipo == "tecnico":
        return render_template("pagina_inicial_tecnico.html")
    else:
        return redirect(url_for("index"))

@app.route("/pagina_inicial_cliente")
@login_required
def pagina_inicial_cliente():
    if current_user.tipo == "cliente":
        return render_template("pagina_inicial_cliente.html")
    else:
        return redirect(url_for("index"))
        
@app.route("/pagina_inicial_gestor")
@login_required
def pagina_inicial_gestor():
    if current_user.tipo == "gestor":
        return render_template("pagina_inicial_gestor.html")
    else:
        return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index'))

@app.route("/novo_conteudo", methods=['POST', 'GET'])
@login_required
def novo_conteudo():
    if current_user.tipo == "gestor":
        return redirect(url_for('novo_conteudo_gestor'))
    if current_user.tipo == "cliente":
        flash('Você não tem permissão para acessar essa página', 'erro')
        return redirect(url_for('pagina_inicial'))

    msg = ""

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        nome_tecnico = current_user.nome
        permissoes = request.form['permissoes']
        data_hora_atual = request.form['data_hora']


        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO conteudo (titulo, descricao, nome_tecnico, permissoes, data_hora) VALUES (%s, %s, %s, %s, %s)', (titulo, descricao, nome_tecnico, permissoes, data_hora_atual))
            conn.commit()
            cursor.close()
            conn.close()
            msg = "Salvo com sucesso!"
        
        except Exception as erro:
            msg = f"Erro ao salvar: {str(erro)}"

    data_hora_atual = data_hora()

    return render_template("novo_conteudo.html", msg=msg, data_hora_atual=data_hora_atual)

@app.route("/novo_conteudo_gestor", methods=['POST', 'GET'])
@login_required
def novo_conteudo_gestor():
    if current_user.tipo == "tecnico":
        return redirect(url_for('novo_conteudo'))
    if current_user.tipo != "gestor":
        flash('Você não tem permissão para acessar essa página', 'erro')
        return redirect(url_for('pagina_inicial'))
    

    msg = ""

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        nome_tecnico = request.form['nome_tecnico']
        permissoes = request.form['permissoes']
        data_hora_atual = request.form['data_hora']

        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO conteudo (titulo, descricao, nome_tecnico, permissoes, data_hora) VALUES (%s, %s, %s, %s, %s)', (titulo, descricao, nome_tecnico, permissoes, data_hora_atual))
            conn.commit()
            cursor.close()
            conn.close()
            msg = "Salvo com sucesso!"
        
        except Exception as erro:
            msg = f"Erro ao salvar: {str(erro)}"

    data_hora_atual = data_hora()

    return render_template("novo_conteudo_gestor.html", msg=msg, data_hora_atual=data_hora_atual)

@app.route("/editar_conteudo", methods=['POST', 'GET'])
@login_required
def editar_conteudo():
    if current_user.tipo != "gestor":
        flash('Você não tem permissão para acessar essa página', 'erro')
        return redirect(url_for('pagina_inicial'))

    msg = ""

    if request.method == 'POST':
        id = request.form['id']
        categoria = request.form['categoria']
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        nome_tecnico = request.form['nome_tecnico']
        permissoes = request.form['permissoes']
        # Implementar pegar horario automaticamente
        

        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO conteudo (titulo, categoria, descricao, nome_tecnico, permissoes) VALUES (%s, %s, %s, %s, %s)', (titulo, categoria, descricao, nome_tecnico, permissoes))
            conn.commit()
            cursor.close()
            conn.close()
            msg = "Salvo com sucesso!"
        
        except Exception as erro:
            msg = f"Erro ao salvar: {str(erro)}"

    return render_template("editar_conteudo.html", msg=msg)

@app.route("/sugestao", methods=['POST', 'GET'])
@login_required
def sugestao():

    flash("Essa página não existe!", "erro")
    return redirect(url_for('pagina_inicial'))

    '''msg = ''

    if request.method=='POST':
        nome = request.form['titulo']
        descricao = request.form['descricao']
        email = request.form['email']

        if not nome or not descricao or not email:
            flash("Todos os campos são obrigatórios", "erro")
            return redirect(url_for('sugestao'))
        
    try:
        pass

    except Exception as erro:
        msg = f"Erro ao enviar sugestão: {str(erro)}"

    return render_template("sugestao.html", msg = 'Enviado com sucesso!')'''

@app.route("/cadastrar", methods=['POST', 'GET'])
@login_required
def cadastrar():
    msg = ''

    if current_user.tipo != 'gestor':
        flash('Você não tem permissão para acessar essa página', 'erro')
        return redirect(url_for('pagina_inicial'))

    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        email = request.form['email']
        senha = request.form['senha']

        if not nome or not tipo or not email or not senha:
            flash("Todos os campos são obrigatórios", "erro")
            return redirect(url_for('cadastrar'))

        try:
            conn = conectar()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash("Este email já está registrado", "erro")
                conn.close()
                return redirect(url_for('cadastrar'))
            
            
            hashed_password = generate_password_hash(senha)
            cursor.execute('INSERT INTO usuarios(nome, tipo, email, senha) VALUES (%s, %s, %s, %s)', (nome, tipo, email, hashed_password))

            conn.commit()

            msg = 'Cadastrado com Sucesso!'

        except Exception as erro:
            msg = f'Ops, houve um erro: {str(erro)}'
            print(f"Erro: {erro}")

        finally:
            conn.close()

    return render_template("cadastrar.html", msg=msg)



if __name__ == "__main__":
    app.run(debug=True)