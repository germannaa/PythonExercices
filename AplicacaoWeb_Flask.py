from flask import Flask, render_template, redirect, url_for,request
import psycopg2


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cadastrodealuno", methods=["POST", "GET"])
def cadastrodealuno():
    if request.method == "POST":
        conectar = psycopg2.connect(host="localhost",port="5432",database="postgres",user="postgres",password="123")
        cur = conectar.cursor()
        
        user = request.form["nomeAluno"]
        idade = request.form["idade"]
        matricula = request.form["matricula"]

        cur.execute(f"INSERT INTO alunos(nome,idade,matricula) VALUES('{user}','{idade}','{matricula}')")
        
        conectar.commit()
        cur.close()
        conectar.close()

        return redirect(url_for('name3', usr=user))
        #return redirect(url_for('name2', name=user))
    else:
        return render_template("cadastrodealuno.html")
'''    render_template("cadastrodealuno.html")
'''    '''return "Cadastro de alunos! <h1> Tela reservada para construção da pagina de  cadastro de alunos </h1>"'''

'''
@app.route("/<name>")
def name(name):
    return render_template("index.html", content=name, parametro=["ai", "ei", "ou"])'''

@app.route("/admin")
def admin():
    return redirect((url_for("home")))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nome"]
        #Conexao(user, idade, matricula)
        return redirect(url_for('name3', usr=user))
        #return redirect(url_for('name2', name=user))
    else:
        return render_template("login.html")

'''
@app.route("/<usr>")
def name2(usr):
    return f"<h1>{usr}</h1>"'''

@app.route("/<usr>")
def name3(usr):
    return render_template("index3.html", content=usr, parametro=["ai", "ei", "ou"])




if __name__ == "__main__":
    app.run(debug = True)




    
'''Fazer html de cadastro
conectar psycopg'''
