
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

'''
@app.route("/")
def home():
    return "Olá! Aula de Algoritmos usando Flask <h1> Criando pags com Flask </h1>"

if __name__ == "__main__":
    app.run()
'''

@app.route("/")
def home():

    return "Olá! Aula de Algoritmos usando Flask <h1> Criando pags com Flask </h1>"


@app.route("/cadastrodealunos")
def cadastrodealunos():

    return "Cadastro de alunos! <h1> Tela reservada para construção da pagina de  cadastro de alunos </h1>"

'''
return "render_template('FormsPy.html')"
'''

@app.route("/<name>")
def user(name):
    return f'Hello {name}!'

@app.route("/admin")
def admin():
    return redirect((url_for("home")))





if __name__ == "__main__":
    app.run()


    '''3 links:
    1. cadastro -> Form de Cadastro de alunos
    2. informações
    3. Seja bem vindo'''
