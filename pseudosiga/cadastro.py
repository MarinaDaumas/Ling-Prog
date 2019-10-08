from flask import Flask, request, render_template
from aluno import Aluno

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('cadastro.html')


@app.route("/login", methods=['POST'])
def login():

    name = str(request.form["name"])
    password = str(request.form["password"])

    if #apertou o botao de login:
        login = aluno.login(name, password)
        if login:
            return render_template("inscricao_disciplina.html")
        else:
            return render_template("login_incorreto.html")

    if #apertou cadastro:
        return render_template("cadastro.html")


@app.route("/cadastro", methods=['POST'])
def cadastro():

    name = str(request.form["name"])
    password = str(request.form["password"])
    DRE = str(request.form["DRE"])

    aluno.novo_cadastro(name, DRE, password)

    if #apertou cadastrar :
        return render_template("login.html")





if __name__ == "__main__":
    app.run(debug=True)