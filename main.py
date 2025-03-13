from flask import Flask, render_template, request
from flask import redirect, url_for

app = Flask(__name__) #objeto flask

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novo_conteudo", methods=['POST', 'GET'])
def novo_conteudo():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        nome_tecnico = request.form['nome_tecnico']
        permissoes = request.form['permissoes']

        #Implementar conectar e inserir no banco

        return render_template("novo_conteudo.html", msg='Salvo com sucesso!')
    return render_template("novo_conteudo.html")

@app.route("/sugestao", methods=['POST', 'GET'])
def sugestao():
    if request.method=='POST':
        nome = request.form['titulo']
        descricao = request.form['descricao']
        email = request.form['email']

        return render_template("sugestao.html", msg = 'Enviado com sucesso!')
    return render_template("sugestao.html")
        
    


if __name__ == "__main__":
    app.run(debug=True)