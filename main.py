from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug import generate_password_hash, check_password_hash
from conexao_db import conectar
from login import current_user, User, login_manager


app = Flask(__name__) #objeto flask
app.secret_key = 'ASDB1578963' #chave secreta

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['password'], password):
            user_obj = User(id=user['id'], email=user['email'], role=user['role'])
            login_user(user_obj)
            flash("Seja Bem Vindo(a)!", "sucesso")

        if user['role'] == 'gestor':
            return redirect(url_for('pagina_inicial'))
        elif user['role'] == 'tecnico':
            return redirect(url_for('pagina_inicial_tecnico'))
        elif user['role'] == 'cliente':
            return redirect(url_for('pagina_inicial_cliente'))
        
        else:
            flash('Login ou Senha inválido', 'sem sucesso')
    #return render_template("index.html")
    return render_template("pagina_inicial.html")


@app.route("/pagina_inicial_tecnico")
@login_required
def pagina_inicial_tecnico():
    if current_user.role == "tecnico":
        return render_template("pagina_inicial_tecnico.html")
    else:
        return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/pagina_inicial", methods=['POST', 'GET'])
def pagina_inicial():
    return render_template("pagina_inicial.html")

@app.route("/novo_conteudo", methods=['POST', 'GET'])
def novo_conteudo():

    msg = ""

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        nome_tecnico = request.form['nome_tecnico']
        permissoes = request.form['permissoes']
        #Implementar pegar horario automaticamente

        try:
            conn = conectar()
            cursor = conn.cursor()

            sql = 'INSERT INTO conteudo (titulo, descricao, nome_tecnico, permissoes) VALUES (%s, %s, %s, %s)'

            cursor.execute(sql, (titulo, descricao, nome_tecnico, permissoes))
            conn.commit()
            cursor.close()
            conn.close()

            msg = "Salvo com sucesso!"
        
        except Exception as erro:
            msg = f"Erro ao salvar: {str(erro)}"

    return render_template("novo_conteudo.html", msg=msg)

@app.route("/sugestao", methods=['POST', 'GET'])
def sugestao():

    msg = ''

    if request.method=='POST':
        nome = request.form['titulo']
        descricao = request.form['descricao']
        email = request.form['email']
    try:
        pass

    except Exception as erro:
        msg = f"Erro ao enviar sugestão: {str(erro)}"

    return render_template("sugestao.html", msg = 'Enviado com sucesso!')


if __name__ == "__main__":
    app.run(debug=True)